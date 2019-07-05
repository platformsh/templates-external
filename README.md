# Third-Party Platform.sh Templates

This repository includes an index of third-party-maintained project templates for Platform.sh.

To add or update a template definition, please make a Pull Request against this project.  All third party templates are listed in the [`templates`](templates) directory, and are named `PROJECT.template.yaml`.  Add a new file for your project, or if you wish to update an existing template you can do that, too.

The Pull Request will be evaluated by our team, who may offer feedback and request changes before it is accepted.

Use the [`template-definition.yaml`](template-definition.yaml) as a starting point.  It should be reasonably well-documented.  If you have questions, please reach out to the Platform.sh Developer Relations team via the [Platform.sh Slack channel](https://chat.platform.sh/).

Note that you do not need to include the template definition file in your project repository, just this one.  The project repository linked from the template definition file can be any publicly-accessible Git URL.

To create the image URI representing the template, find an SVG formatted logo for your project, [create a data URL](https://dataurl.sveinbjorn.org/#dataurlmaker) of that image and paste the output into `image:`.
