# Object-based attention during scene perception elicits boundary contraction in memory
Journal Article [link](https://rdcu.be/dHWZk).
<br> OSF Repository [link](https://osf.io/mkas7/). 
<br> Beth's website [link](https://elizabethhhall.com).

If you use this code or dataset in you research, please cite this paper. 

```
@article{hall2024object,
  title={Object-based attention during scene perception elicits boundary contraction in memory},
  author={Hall, Elizabeth H and Geng, Joy J},
  journal={Memory \& cognition},
  pages={1--13},
  year={2024},
  publisher={Springer}
}
```

## Abstract

Boundary contraction and extension are two types of scene transformations that occur in memory. In extension, viewers extrapolate information beyond the edges of the image, whereas in contraction, viewers forget information near the edges. Recent work suggests that image composition influences the direction and magnitude of boundary transformation. We hypothesize that selective attention at encoding is an important driver of boundary transformation effects, selective attention to specific objects at encoding leading to boundary contraction. In this study, one group of participants (N = 36) memorized 15 scenes while searching for targets, while a separate group (N = 36) just memorized the scenes. Both groups then drew the scenes from memory with as much object and spatial detail as they could remember. We asked online workers to provide ratings of boundary transformations in the drawings, as well as how many objects they contained and the precision of remembered object size and location. We found that search condition drawings showed significantly greater boundary contraction than drawings of the same scenes in the memorize condition. Search drawings were significantly more likely to contain target objects, and the likelihood to recall other objects in the scene decreased as a function of their distance from the target. These findings suggest that selective attention to a specific object due to a search task at encoding will lead to significant boundary contraction.

## Data

CSV files for the main analyses are included here. The full dataset can be downloaded from the OSF Repository [link](https://osf.io/mkas7/). It contains the drawings done from memory, the 15 scenes used in the experiment with segmentations for the objects in the scenes, eye-tracking fixations from the study phase, and ratings from the 3 online AMT tasks. 

## Code 

<i>Settings</i> defines the directories. <br>
<i>Attention</i> notebook includes code for the eyetracking analyses. 
<br><i>Boundary</i> calculates boundary transformations in the drawings. 
<br><i>Corners</i> is used to define the scale of the scanned in drawings.
<br><i>Location</i> calculates the shift in remembered object location from the memory drawings.
<br><i>Memory</i> includes models for what determines whether an object in the image will be drawn from memory. 
