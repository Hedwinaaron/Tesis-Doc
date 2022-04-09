import ROOT
import numpy as np
import array as arr
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
Entries=tree.GetEntries()


#create and fill the histogram
can1  = ROOT.TCanvas("can1", "hist", 1400,700)
can2 = ROOT.TCanvas("can2", "hist", 1400,700)
can3  = ROOT.TCanvas("can3", "hist", 1400,700)
can4 = ROOT.TCanvas("can4", "hist", 1400,700)
can5 = ROOT.TCanvas("can5", "hist", 1400,700)
can6= ROOT.TCanvas("can6", " hist", 1400,700)
can7= ROOT.TCanvas("can7", "hist", 1400,700)
can8= ROOT.TCanvas("can8", "hist", 1400,700)
can9= ROOT.TCanvas("can9", "hist", 1400,700)
can10= ROOT.TCanvas("can10", "hist", 1400,700)
can11= ROOT.TCanvas("can11", "hist", 1400,700)

h1 = ROOT.TH1D("h1", "Down dGl", 500, 0.0, 500.0)
h2 = ROOT.TH1D("h2", "Up dGl", 500, 0.0, 500.0)
h3= ROOT.TH1D("h3", "Resolution hist", 200, -1, 1)
h4= ROOT.TH1D("h4", "Res Pt_30-40 hist ", 100, -0.1, 0.1)
h5= ROOT.TH1D("h5", "Res Pt_40-50 hist ", 100, -0.1, 0.1)
h6= ROOT.TH1D("h6", "Res Pt_50-70 hist ", 100, -0.1, 0.1)
h7= ROOT.TH1D("h7", "Res Pt_70-100 hist ", 100, -0.1, 0.1)
h8= ROOT.TH1D("h8", "Res Pt_100-150 hist ", 100, -0.1, 0.1)
h9= ROOT.TH1D("h9", "Res Pt_150-200 hist ", 100, -0.1, 0.1)
h10= ROOT.TH1D("h10", "Res Pt_200-350 hist ", 100, -0.1, 0.1)
h11= ROOT.TH1D("h11", "Res Pt_350-500 hist ", 100, -0.1, 0.1)

#relevant variables
entry_down=0
entry_up=0
downdgl_pt=0
updgl_pt=0
k=-1
inv_Uppt=0
inv_Downpt=0
res=0
pt_bin=np.array([30,40,50,70,100,150,200,350,500])


#Events selection and histogram filling
for i in range(0,Entries):
    tree.GetEntry(i) 
    pair_dphi= abs(tree.tag_phi-tree.probe_updgl_phi)
    pair_dphi_reduced= abs(pair_dphi - 3.141592 * (1 + (pair_dphi-3.141592)/abs(pair_dphi-3.141592)))
    tag_abseta= abs(tree.tag_eta)
    if tree.HLT_L2Mu10_NoVertex_NoBPTX3BX_v == 1 and tree.tag_pt > 20 and tag_abseta < 0.9: 
        
        if tree.tag_phi < -0.6 and tree.tag_phi > -2.6 and tree.probe_downdgl_pt >20 :
            entry_down=i
            downdgl_pt = tree.probe_downdgl_pt
        
            
    
        if  tree.probe_isUpdGlobal == 1 and tree.probe_updgl_pt > 20 and pair_dphi_reduced > 2.8:
            entry_up=i
            updgl_pt = tree.probe_updgl_pt
            
               
                
        if entry_up==entry_down:
            if updgl_pt==0 or downdgl_pt==0:
                continue
            print("Event", i)
            h1.Fill(downdgl_pt)
            print("Down dGl",downdgl_pt)
            h2.Fill(updgl_pt)
            print("Up dGl",updgl_pt)
            
            inv_Uppt=1/updgl_pt
            inv_Downpt=1/downdgl_pt
            res=((inv_Uppt)-(inv_Downpt))/(np.sqrt(2)*(inv_Downpt))
            h3.Fill(res)
            k+=1
            print(k,inv_Uppt,inv_Downpt)
            
            if pt_bin[0]<updgl_pt<pt_bin[1]:
                h4.Fill(res)
            
            if pt_bin[1]<updgl_pt<pt_bin[2]:

                h5.Fill(res)
                
            if pt_bin[2]<updgl_pt<pt_bin[3]:

                h6.Fill(res)
                
            if pt_bin[3]<updgl_pt<pt_bin[4]:

                h7.Fill(res)
            
            if pt_bin[4]<updgl_pt<pt_bin[5]:

                h8.Fill(res)
            
            if pt_bin[5]<updgl_pt<pt_bin[6]:
                h9.Fill(res)
            
            
            if pt_bin[6]<updgl_pt<pt_bin[7]:
                h10.Fill(res)
            
            
            if pt_bin[7]<updgl_pt<pt_bin[8]:
                h11.Fill(res)
                

#creating output root file    
outHistFile = ROOT.TFile.Open ( "Res_hist.root" ,"RECREATE")
outHistFile.cd()

#Hstograms pf pt distribution in upper and lower half
can1.cd()
h1.Write("down_ndgl_pt")
h1.Draw()
can1.SaveAs("plots/histograms/down_ndgl_pt.png")

can2.cd()
h2.Write("up_dgl_pt")
h2.Draw()
can2.SaveAs("plots/histograms/up_dgl_pt.png")

#histogram of resolution distribution
can3.cd()
h3.Write("Resolutions_hist")
h3.Draw()
can3.SaveAs("plots/histograms/Resolutions_hist.png")
#Histograms of resolution distribution per pt interval 

h4.Write("pt_30-40_hist")
can4.cd()
h4.Fit("gaus")
h4.Draw()
can4.SaveAs("plots/histograms/pt_30-40_hist.png")

h5.Write("pt_40-50_hist")
can5.cd()
h5.Fit("gaus")
h5.Draw()
can5.SaveAs("plots/histograms/pt_40-50_hist.png")

h6.Write("pt_50-70_hist")
can6.cd()
h6.Fit("gaus")
h6.Draw()
can6.SaveAs("plots/histograms/pt_50-70_hist.png")

h7.Write("pt_70-100_hist")
can7.cd()
h7.Fit("gaus")
h7.Draw()
can7.SaveAs("plots/histograms/pt_70-100_hist.png")


h8.Write("pt_100-150_hist")
can8.cd()
h8.Fit("gaus")
h8.Draw()
can8.SaveAs("plots/histograms/pt_100-150_hist.png")

h9.Write("pt_150-200_hist")
can9.cd()
h9.Fit("gaus")
h9.Draw()
can9.SaveAs("plots/histograms/pt_150-200_hist.png")

h10.Write("pt_200-350_hist")
can10.cd()
h10.Fit("gaus")
h10.Draw()
can10.SaveAs("plots/histograms/pt_200-350_hist.png")

h11.Write("pt_350-500_hist")
can11.cd()
h11.Fit("gaus")
h11.Draw()
can11.SaveAs("plots/histograms/pt_350-500_hist.png")
#closing output file
outHistFile.Close()



