# Hub Enabler

Welcome to the `hub` Horizontal Enabler.

This is the central service for project creation, community coordination, and ecosystem-wide search.

This is a monorepo that contains the three core components of the `hub` enabler:

  * **`/api`**: The backend API service (e.g., Python/Flask).
  * **`/app`**: The frontend web application (e.g., React/Node.js).
  * **`/website`**: The Docusaurus-based documentation site for this enabler.
  * **`/tests`**: The intra-repo integration tests that verify `/api` and `/app` work together.

## 🚀 Getting Started (Local Development)

This repository is configured to use **DevContainers** for a one-click setup, powered by our centralized `ecosystem-devtools` images.

1.  Make sure you have([https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)) installed and running.
2.  Install the([https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)) in VS Code.
3.  Clone this repository: `git clone https://github.com/nova-ecosystem/hub.git`
4.  Open the cloned folder in VS Code.
5.  A pop-up will appear: "Folder contains a Dev Container... Reopen in Container?". Click **"Reopen in Container"**.

This will instantly download the pre-built `dev-python` and `dev-node` images and start all three services (`api`, `app`, `website`) in an integrated environment.