"""
heapplot - AI Lab Assignment Code Reference Package
====================================================

A Python package that prints the complete source code of classic AI algorithms
from university lab assignments directly to your terminal.

Built to automate AI game engine logic references for VR headset development.

Available Functions
-------------------
Assignment 1 - Search Algorithms:
    heapplot.bfs()             - Breadth First Search
    heapplot.dfs()             - Depth First Search
    heapplot.dls()             - Depth Limited Search

Assignment 2 - Heuristic Search:
    heapplot.bestfirst()       - Best First Search
    heapplot.astar()           - A* Algorithm (graph)

Assignment 3 - Puzzle Solving:
    heapplot.puzzle8()         - 8-Puzzle Problem (A* with misplaced tiles)

Assignment 4 - Constraint Satisfaction:
    heapplot.nqueens()         - N-Queens Problem (CSP with Backtracking)

Assignment 5 - Local Search:
    heapplot.hillclimbing()    - Hill Climbing Algorithm

Assignment 6 - Game Tree Search:
    heapplot.alphabeta()       - Alpha-Beta Pruning (Minimax)

Assignment 7 - Planning with Search:
    heapplot.missionarycannibals() - Missionaries & Cannibals (A*)

Assignment 8 - AI Planning:
    heapplot.goalstack()       - Goal Stack Planning (Blocks World)

Assignment 9 - Knowledge Representation:
    heapplot.forwardchaining() - Forward Chaining Inference

Assignment 10 - Probabilistic AI:
    heapplot.bayesian()        - Bayesian Network (Student Exam Performance)

Usage
-----
    import heapplot

    heapplot.bfs()
    heapplot.alphabeta()
    heapplot.bayesian()
    # ... etc

Or use heapplot.help() to list all available functions.
"""

from .bfs import bfs
from .dfs import dfs
from .dls import dls
from .bestfirst import bestfirst
from .astar import astar
from .puzzle8 import puzzle8
from .nqueens import nqueens
from .hillclimbing import hillclimbing
from .alphabeta import alphabeta
from .missionarycannibals import missionarycannibals
from .goalstack import goalstack
from .forwardchaining import forwardchaining
from .bayesian import bayesian

__version__ = "1.0.1"
__author__ = "heapplot"
__description__ = (
    "AI Lab Assignment Code Reference Package - "
    "Automation toolkit for AI game engine logic in VR headset development"
)

__all__ = [
    "bfs",
    "dfs",
    "dls",
    "bestfirst",
    "astar",
    "puzzle8",
    "nqueens",
    "hillclimbing",
    "alphabeta",
    "missionarycannibals",
    "goalstack",
    "forwardchaining",
    "bayesian",
    "help",
]


def help():
    """
    Print all available heapplot functions with their descriptions.
    Usage: heapplot.help()
    """
    print("""
╔══════════════════════════════════════════════════════════════════════════╗
║                    heapplot - AI Lab Code Reference                     ║
║          Automation Toolkit for VR Headset AI Game Engine Logic         ║
╚══════════════════════════════════════════════════════════════════════════╝

 Assignment 1 - Search Algorithms:
   heapplot.bfs()                  Breadth First Search
   heapplot.dfs()                  Depth First Search
   heapplot.dls()                  Depth Limited Search

 Assignment 2 - Heuristic Search:
   heapplot.bestfirst()            Best First Search
   heapplot.astar()                A* Algorithm

 Assignment 3 - Puzzle Solving:
   heapplot.puzzle8()              8-Puzzle Problem (A* search)

 Assignment 4 - Constraint Satisfaction:
   heapplot.nqueens()              N-Queens Problem (CSP / Backtracking)

 Assignment 5 - Local Search:
   heapplot.hillclimbing()         Hill Climbing Algorithm

 Assignment 6 - Game Tree Search:
   heapplot.alphabeta()            Alpha-Beta Pruning (Minimax)

 Assignment 7 - Planning with Search:
   heapplot.missionarycannibals()  Missionaries & Cannibals (A*)

 Assignment 8 - AI Planning:
   heapplot.goalstack()            Goal Stack Planning (Blocks World)

 Assignment 9 - Knowledge Representation:
   heapplot.forwardchaining()      Forward Chaining Inference Engine

 Assignment 10 - Probabilistic AI:
   heapplot.bayesian()             Bayesian Network

──────────────────────────────────────────────────────────────────────────
  Call any function to print its full source code to the terminal.
  Example: heapplot.alphabeta()
""")
