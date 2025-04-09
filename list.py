import os
import glob
import yaml

outputFile = "{0}/list.yaml".format(os.getcwd())
templates = glob.glob("{0}/templates/*.yaml".format(os.getcwd()))
dopPrefix = "https://console.platform.sh/projects/create-project?template=https://raw.githubusercontent.com/platformsh/templates-external/master"

# Hardcode runtimes for now.
runtimes = {
    "OpenideaL": "php",
    "Pizzly": "nodejs",
    "redirection.io": "golang",
    "Restyaboard": "php",
    "Sylius": "php",
    "Symfony 5.4/webapp": "php",
    "Symfony 6.2/webapp": "php",
    "Symfony 6.3/demo": "php",
    "Symfony 6.3/webapp": "php",
    "Varbase (Drupal 10)": "php",
    "Zabbix": "php",
}
uniqueRuntimes = list(set(list(runtimes.values())))
data = dict([(key, []) for key in uniqueRuntimes])

for templateDef in templates:
    with open(templateDef) as file:
        try:
            # Get the data.
            templateData = yaml.safe_load(file)
            # Define the repository.
            repoParts = templateData['initialize']['repository'].split(".git@")
            if len(repoParts) == 1:
                repo = repoParts[0].split(".git")[0]
            else:
                repo = "{0}/tree/{1}".format(repoParts[0], repoParts[1])
            # Define object pulling from template.yamls.
            entry = {
                "shortname": templateData['info']['id'],
                "name": templateData['info']['name'],
                "repo": repo,
                "description": templateData['info']['description'],
                "image": templateData['info']['image'],
                "deploy": "{0}/{1}".format(dopPrefix, templateDef.split("/templates-external/")[1]),
                "content": templateData['info']['notes'][0]['content'],
                "tags": templateData['info']['tags']
            }
            # Append to the runtime key.
            currentRuntime = runtimes[templateData['info']['name']]
            data[currentRuntime].append(entry)
        except yaml.YAMLError as exc:
            print(exc)

# Output.
with open(outputFile, 'w') as file:
    yaml.dump(data, file)
