from loguru import logger  # noqa
import click
import json
from scrapegraphai.graphs import SmartScraperGraph  # type: ignore[import-untyped]


@logger.catch
@click.command(
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.option(
    "--model",
    envvar=["OLLAMA_MODEL"],
    type=str,
    required=True,
    multiple=False,
    help="The ollama model to use for the scraper config.",
)
@click.option(
    "--prompt",
    "-p",
    type=str,
    required=False,
    multiple=False,
    show_default=True,
    default=["Describe the page."],
    help="The prompt to use.",
)
@click.option(
    "--source",
    "-s",
    type=str,
    required=True,
    multiple=False,
    help="The source to use.",
)
def cli(model: str, prompt: str, source: str):
    graph_config = {
        "llm": {
            "model": f"ollama/{model}",
            "format": "json",
            "base_url": "http://ollama:11434",
        },
        "verbose": False,
        "headless": True,
    }

    smart_scraper_graph = SmartScraperGraph(
        prompt=prompt, source=source, config=graph_config
    )

    # Run the pipeline
    result = smart_scraper_graph.run()

    print(json.dumps(result, indent=4))
