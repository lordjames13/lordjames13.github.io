# GearLab public website

Website: https://lordjames13.github.io/

This repository holds a reviewed public website package and its deployment workflow. It is hosted on GitHub Pages using the free github.io address. Source development is maintained separately.

## Future updates

1. Edit and check the development project.
2. From the development project root, run `python resources/code/package_github_pages.py --output ../gearlab-pages-public/site.zip`.
3. Replace `site.zip` in this repository and commit it to `main`.
4. Wait for the **Publish GearLab** workflow to succeed. It verifies every packaged file against `public_release.json`, excludes the original private résumé, and deploys only the extracted public website.
5. Verify the website, comparison view, research directory and public résumé anonymously. The `public_release.json` URL exposes the deployed file hashes and release ID.

The archive includes the public résumé with the current website address, research downloads and static website assets. It does not include the original private résumé, development repository history or credentials. The current site remains live if an archive validation step fails before deployment.

No purchased domain is configured.
