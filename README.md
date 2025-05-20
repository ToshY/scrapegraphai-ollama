# 🕷️ ScrapeGraphAI with Ollama 🦙 in Compose 🐋

Basic example repository showing how to use [ScrapeGraphAI](https://github.com/ScrapeGraphAI/Scrapegraph-ai) with [Ollama](https://hub.docker.com/r/ollama/ollama) in docker compose.

## 🧰 Getting Started

### ‼️ Prerequisites

* [Docker Compose V2](https://docs.docker.com/compose/install/)
* [Task (3.43+)](https://taskfile.dev/installation/) (optional, but recommended)

## 📝 Quickstart

Up the `ollama` service.

```shell
task up
```

> [!NOTE]
> The default model `ollama3.2` will be pulled inside the `ollama` service. You can create your own `.env` file
> and change the `OLLAMA_MODEL` variable to the desired model (see the [Model library](https://github.com/ollama/ollama?tab=readme-ov-file#model-library)).

> [!TIP]
> If you want to use GPU capabilities, follow the instructions in the [ollama/ollama](https://hub.docker.com/r/ollama/ollama) docker repository.
> Afterward, you can create a `compose.override.yaml` to star the `ollama` service with GPU options.
> 
> Example for Nvidia GPU:
> ```yaml
> services:
>   ollama:
>     deploy:
>       resources:
>         reservations:
>           devices:
>             - driver: nvidia
>               count: all
>               capabilities: [gpu]
> ```

Then run the `scrapegraph` module.

```shell
task run p="Describe the page" s="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

Response.

```json
{
    "content": "The webpage appears to be a YouTube video page for the song 'Never Gonna Give You Up' by Rick Astley. The page includes information such as the video's title, channel, and views. There is also a link to a biography and an audiobook introduction. The page has a playlist section where viewers can add videos, but there seems to be a technical issue with sharing functionality."
}
```

> [!IMPORTANT]
> If you are done and no longer need to use ollama and its volume, make sure to remove it.
> ```shell
> task down -- -v --remove-orphans
> # or
> docker compose down -v --remove-orphans
> ```


## 🛠️ Contribute

### Requirements

* ☑️ [Pre-commit](https://pre-commit.com/#installation).
* 🐋 [Docker Compose V2](https://docs.docker.com/compose/install/)
* 📋 [Task 3.37+](https://taskfile.dev/installation/)

## ❕ License

This repository comes with a [BSD 3-Clause License](./LICENSE).