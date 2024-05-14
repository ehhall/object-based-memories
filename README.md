# Object-based attention during scene perception elicits boundary contraction in memory
Journal Article [link](https://rdcu.be/dHWZk).
<br> OSF Repository [link](https://osf.io/mkas7/). 
<br> Please contact ehhall @ ucdavis . edu with questions. 

This repository contains code to work with the dataset from Hall & Geng (2024). If you use this code or dataset in you research, please cite this paper. 

```
Hall, E.H., Geng, J.J.
Object-based attention during scene perception elicits boundary contraction in memory.
Mem Cogn (2024). https://doi.org/10.3758/s13421-024-01540-9
```

## Abstract

Boundary contraction and extension are two types of scene transformations that occur in memory. In extension, viewers extrapolate information beyond the edges of the image, whereas in contraction, viewers forget information near the edges. Recent work suggests that image composition influences the direction and magnitude of boundary transformation. We hypothesize that selective attention at encoding is an important driver of boundary transformation effects, selective attention to specific objects at encoding leading to boundary contraction. In this study, one group of participants (N = 36) memorized 15 scenes while searching for targets, while a separate group (N = 36) just memorized the scenes. Both groups then drew the scenes from memory with as much object and spatial detail as they could remember. We asked online workers to provide ratings of boundary transformations in the drawings, as well as how many objects they contained and the precision of remembered object size and location. We found that search condition drawings showed significantly greater boundary contraction than drawings of the same scenes in the memorize condition. Search drawings were significantly more likely to contain target objects, and the likelihood to recall other objects in the scene decreased as a function of their distance from the target. These findings suggest that selective attention to a specific object due to a search task at encoding will lead to significant boundary contraction.

## Data

The dataset can be downloaded from the OSF Repository [link](https://osf.io/mkas7/). It contains the drawings done from memory, the 15 scenes used in the experiment with segmentations for the objects in the scenes, eye-tracking fixations from the study phase, and ratings from the 3 online AMT tasks. 

## Code 

The settings file defines the directories. Attention.ipynb notebook includes code for the eyetracking analyses. Boundary.ipynb calculates boundary transformations in the drawings (Corners.ipynb is used to define the scale of the scanned in drawings). Location.ipynb calculates the shift in remembered object location from the memory drawings. Memory.ipynb includes models for what determines whether an object in the image will be drawn from memory. 
