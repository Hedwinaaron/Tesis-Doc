import ROOT
import sys
if len( sys.argv ) != 2:
  print"USAGE: %s <input file >"%( sys.argv [0])
  sys.exit (1)
 #input the name of the root file
inFileName = sys.argv[1]

#Open root file and get branch
inFile = ROOT.TFile.Open( inFileName ," READ ")
tree = inFile.Get ("muon/Events")
print "Reading from ", inFileName
Branch=tree.GetBranch("run")
Entries=Branch.GetEntries()

#create and fill the histogram (incomplete)
can  = ROOT.TCanvas("can", "histograms   ", 1400,700)
h1 = ROOT.TH1D("h1", "h1 title", 1, 0.0, 3.0)
Branch.Clone("h1") 
h1.Draw()
can.SaveAs("histogram.png")
  
