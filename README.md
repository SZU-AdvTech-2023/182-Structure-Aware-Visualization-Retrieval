## Structure-aware Visualization Retrieval

Code for paper [*Structure-aware Visualization Retrieval*](https://dl.acm.org/doi/10.1145/3491102.3502048):

```
@inproceedings{li2022structure,
  title={Structure-aware visualization retrieval},
  author={Li, Haotian and Wang, Yong and Wu, Aoyu and Wei, Huan and Qu, Huamin},
  booktitle={Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems},
  pages={1--14},
  year={2022}
}
```

### How to run the code
1. run `./svg_processing.sh` and `python graph_construction.py` in `svg_processing` folder
2. run `./train.sh` in `simsiam` and `infograph` folders
3. run `./embed.sh` in `simsiam` and `infograph` folders after training models
4. run `python evaluation.py` under the main directory

### Required packages
- Python: DGL 0.6.1, PyTorch 1.9.0

- JavaScript: d3-regression 1.3.9, svg-parser 2.0.4, cssjson 2.1.3, svg-path-bounds 1.0.2, svg-path-properties 1.0.11, svg-pathdata 6.0.0

### Reference
[1] SimSiam: https://github.com/facebookresearch/simsiam

[2] InfoGraph-DGL: https://github.com/dmlc/dgl/tree/master/examples/pytorch/infograph