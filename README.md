# gsio-net research

> This is an experiment (in-progress) for generating synthetic research in emerging markets.

## Prerequisites
- Anaconda

## Quickstart

1. Clone this repository
2. Run `setup.sh`
3. Follow instructions in [Usage](#usage)

## Configuration

The project uses a `config.ini` file to configure various aspects of the simulation, including:
- OpenAI API settings
- Model parameters
- Simulation settings
- Logging configuration

## Usage

Run the simulation with:

```
python main.py
```

This will create a virtual world with predefined agents (Diego, Aisha, Elena, and Nakamura) and start a conversation between them.

## Agents

Agents are defined as JSON in the `agents/` directory. Each agent file should follow the structure shown in the existing agent files and `agents.py`

## Acknowledgements
- [TinyTroupe](https://microsoft.github.io/TinyTroupe)