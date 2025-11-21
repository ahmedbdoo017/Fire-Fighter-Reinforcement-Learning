"""
Main entrypoint for the FireFighter Reinforcement Learning Project.

This file does NOT run training directly.
Instead, it guides the user to the correct folders:
- env/     -> for environment logic and environment settings
- models/  -> for building RL models (DQN, Policy Gradient) from scratch
- testing/ -> for testing trained agents inside the UI environment

Choose a mode and this script will show you exactly where to go.
"""

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="FireFighter RL Project Navigation Tool"
    )

    parser.add_argument(
        "--mode",
        type=str,
        required=True,
        choices=[
            "env",
            "dqn_model",
            "pg_model",
            "test_dqn",
            "test_pg"
        ],
        help=(
            "Choose what you want to explore:\n"
            " env        -> Environment logic & reward shaping\n"
            " dqn_model  -> Build your DQN from scratch\n"
            " policy_gredientt -> Build & train your Policy Gradient model\n"
            " test_dqn   -> Train & Test DQN agent + UI to show how agent work in enviroment\n"
            " test_pg    -> Test Policy Gradient agent + UI to show how agent work in enviroment\n"
        )
    )

    args = parser.parse_args()

    if args.mode == "env":
        print("\n🌍 ENVIRONMENT SELECTED")
        print("Go to:  src/env/fire_fighter_env.py")
        print("There you can modify:")
        print(" - grid rules")
        print(" - fire spreading logic")
        print(" - rewards & penalties")
        print(" - agent movement\n")

    elif args.mode == "dqn_model":
        print("\n DQN MODEL SELECTED")
        print("Go to:  src/models/dqn_model.py")
        print("Inside you can:")
        print(" - see full DQN architecture")
        print(" - understand forward pass")
        print(" - training steps")
        print(" - save/load model logic\n")

    elif args.mode == "pg_model":
        print("\n🧠 POLICY GRADIENT MODEL SELECTED")
        print("Go to:  src/models/policy_gredientt.py")
        print("There you will see:")
        print(" - PG model architecture")
        print(" - action sampling")
        print(" - training loop\n")

    elif args.mode == "test_dqn":
        print("\n🎮 TESTING DQN AGENT")
        print("Go to:  src/testing/Test_DQN.ipynb")
        print("There you can:")
        print(" - load trained DQN model")
        print(" - run the agent in the UI")
        print(" - visualize movements\n")

    elif args.mode == "test_pg":
        print("\n🔥 TESTING POLICY GRADIENT AGENT")
        print("Go to:  src/testing/Test_PolicyGradient.ipynb")
        print("There you can:")
        print(" - load trained PG model")
        print(" - run the agent inside the UI")
        print(" - observe behavior & reward trends\n")

    else:
        print("❌ Unknown mode!")


if __name__ == "__main__":
    main()
