# notes

- Nexus is a centralized software used to store, manage and control software artifacts (Any file produced as a result of the software build process) which are used during software development like maven, npm, pypi (pip), docker images etc.
- Think like: I send my code to git repo. I send my build to nexus repo.
- It downloads once and all other users will get the packages from it (like a cache, mirror server). This is perfect because: network optimization, faster build, overall control and security (perfect for air-gapped systems)
- For overall control and security: we can trigger AV scan for new downloaded artifacts once than distribute it. if it is malicious block it.

- There are 3 types of repos: Hosted: you store your own artifacts. Proxy: cache artifacts from external repositories. Group: you do both. good for simplicity.
- 