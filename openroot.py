import ROOT
import numpy as np
import array as arr
import sys
def histogram(htitle, nbins, lowxlim, maxxlim, ent,values):
    c1  = ROOT.TCanvas("c1", "histogram", 1400,700)
    h1 = ROOT.TH1D("h1", htitle, int(nbins), int(lowxlim), int(maxxlim))
    for i in range(0,int(ent)):
        h1.Fill(values)
    h1.Draw()
    c1.SaveAs("histogram.png")

if len( sys.argv ) != 2:
  print"USAGE: %s <input file >"%( sys.argv [0])
  sys.exit (1)
 #input the name of the root file
inFileName = sys.argv[1]

#Open root file and get branch
inFile = ROOT.TFile.Open( inFileName ," READ ")
tree = inFile.Get ("muon/Events")
print "Reading from ", inFileName      
#Branch=tree.GetBranch("run")
#Branch=tree.GetBranch("probe_pt")
Entries=tree.GetEntries()


#h1create and fill the histogram
can  = ROOT.TCanvas("can", "histograms", 1400,700)
can2  = ROOT.TCanvas("can2", "histogramss", 1400,700)
h1 = ROOT.TH1D("h1", "Down dGl", 700, -200.0, 500.0)
h2 = ROOT.TH1D("h2", "Up dGl", 700, -200.0, 500.0)
updgl_pt=np.empty(52, dtype = float)
for i in range(0,Entries):
    tree.GetEntry(i) 
    pair_dphi= abs(tree.tag_phi-tree.probe_updgl_phi)
    pair_dphi_reduced= abs(pair_dphi - 3.141592 * (1 + (pair_dphi-3.141592)/abs(pair_dphi-3.141592)))
    
    #event slectrion criteria 
    if tree.HLT_L2Mu10_NoVertex_NoBPTX3BX_v == 1 and tree.tag_pt > 20 and tree.tag_isdGlobal == 1 and tree.tag_phi < -0.6 and tree.tag_phi > -2.6 and tree.tag_eta < 0.9and tree.isMC == 1:
        print("Event", i)
        
        if tree.tag_phi < -0.6 and tree.tag_phi > -2.6:
            downdgl_pt = tree.tag_pt
            print("Down dGl",downdgl_pt)
            h1.Fill(downdgl_pt)
        
        if tree.probe_isUpdGlobal == 1 and tree.probe_updgl_pt > 20 and pair_dphi_reduced > 2.8:
            updgl_pt = tree.tag_pt
            h2.Fill(updgl_pt)    
            print("Up dGl",updgl_pt)
            
            
            
            
            

        




can.cd()
h1.Draw()
can.SaveAs("downdgl_pt.png")

can2.cd()    
h2.Draw()
can2.SaveAs("updgl_pt.png")

