# Tesis-Doc #

The openroot.py script takes as input output_25.root, containing  the events,  and runs the event selection. To run the script 


```bash
python openroot.py output_25.root
```
and gives as output the file Res_hist.root, containing the histograms showing the events that passed the event selection. To calculate the resolution can be calculated running

```bash
python dgl_ptmuond.py Res_hist.root
```
