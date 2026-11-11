# hello-agent

An agent built with the [Mistral Agents SDK](https://docs-internal-frameworks.mistral.ai/agents-sdk). The agent is in `main.py`.

Set `MISTRAL_API_KEY` in `.env`, with a key from Studio's [API keys](https://console.mistral.ai/api-keys)
page, unless `agents init` already did. `.env` is git-ignored: never commit it. If you export
`MISTRAL_API_KEY` in your shell instead, it takes precedence over `.env`. Then:

```bash
uv run --env-file .env agents info     # show what the CLI loads
uv run --env-file .env agents chat     # chat with the agent in this process
uv run --env-file .env agents serve    # run it as a durable worker
uv run --env-file .env agents deploy   # deploy it as a managed agent
```

`agents deploy` builds the commit you pushed: the project must be in a GitHub repository, and the
GitHub Connector must be enabled on your Mistral account in Studio.
