import Ajv from 'ajv';
import { CodeMaker } from 'codemaker';

// we just need the types from json-schema
// eslint-disable-next-line import/no-extraneous-dependencies
import { JSONSchema4 } from 'json-schema';

import { TypeGenerator } from 'json2jsii';

import { SafeReviver } from '../reviver';
import { download, safeParseJson } from '../util';
import { GenerateOptions, ImportBase } from './base';
import { ApiObjectDefinition, emitHeader, generateConstruct } from './codegen';


export function safeParseJsonSchema(text: string): JSONSchema4 {
    console.log('hello');
    const reviver = new SafeReviver({
      allowlistedKeys: ['$ref', '$schema'],
      sanitizers: { description: SafeReviver.DESCRIPTION_SANITIZER },
    });
    console.log(text);
    const schema = safeParseJson(text, reviver);
    console.log(schema);
    const ajv = new Ajv();
    ajv.addFormat("byte", {
        type: "number",
        validate: (x: number) => x >= 0 && x <= 255 && x % 1 == 0,
      })
    ajv.addFormat("date-time", {
        type: "string",
        validate: () => true
    })
    ajv.addFormat("int64", { type: "string", validate: () => true});
    ajv.compile(schema);
    return schema;
  }



export class ImportKotsApi extends ImportBase {
  public get moduleNames() {
    return ['kots'];
  }



  protected async generateTypeScript(code: CodeMaker, moduleName: string, options: GenerateOptions) {
    const schemas = await downloadSchema();

    if (moduleName !== 'kots') {
      throw new Error(`unexpected module name "${moduleName}" when importing kots types (expected "kots")`);
    }

    const typeGenerator = new TypeGenerator({
        definitions: schemas,
        renderTypeName: (def: string) => {
        return def;
        },
    });


    for (const schemaName in schemas) {
        const prefix = options.classNamePrefix ?? 'KotsApi';
        const schema = schemas[schemaName];
        const o: ApiObjectDefinition = {
            custom: false, // not a CRD
            fqn: 'kots.api.' + schemaName,
            group: 'v1beta1',
            kind: schemaName[0].toUpperCase() + schemaName.slice(1),
            version: '',
            schema: schema,
            prefix,
        }

        typeGenerator.addDefinition(o.fqn, { $ref: `#/definitions/${schemaName}` });

        // emit construct types (recursive)
        generateConstruct(typeGenerator, o);

    }

    emitHeader(code, false);
    code.line(typeGenerator.render());
  }
}

async function downloadSchema() {
    const kotskinds = [
        'airgap',
        'application',
        'config',
        'configvalues',
        'helmchart',
        'identity',
        'identityconfigs',
        'ingressconfigs',
        'installation',
        'license',
    ]

    var schemas: {[k: string]: JSONSchema4} = {};
    for (const k of kotskinds) {
        const url = `https://raw.githubusercontent.com/replicatedhq/kots/main/kotskinds/schemas/${k}-kots-v1beta1.json`;
        const output = await download(url);
        const schema = safeParseJsonSchema(output) as JSONSchema4;
        schemas[k] = schema;
    }
    return schemas;

}