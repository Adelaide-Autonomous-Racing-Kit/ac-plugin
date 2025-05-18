# AC Plugin
Asseto Corsa python plugin for AARK

## Prerequisites
This plugin requires Custom Shaders Patch to be installed.

## Installation
Copy the `AARK` folder into your Assetto Corsa install directory under `assettocorsa/apps/python`.
Activate the application in Assetto Corsa via your launcher of choice.

## Usage
Once installed the application will allow client socket connections on localhost:6337.
Sending the command `b'reset_car'` will place the car back on the racing line nearby to its current location.

## Citation
If you use this work in your research or quote our baselines please cite us in your work:
```BibTeX
@misc{bockman2024aarkopentoolkitautonomous,
      title={AARK: An Open Toolkit for Autonomous Racing Research}, 
      author={James Bockman and Matthew Howe and Adrian Orenstein and Feras Dayoub},
      year={2024},
      eprint={2410.00358},
      archivePrefix={arXiv},
      primaryClass={cs.RO},
      url={https://arxiv.org/abs/2410.00358}, 
}
```