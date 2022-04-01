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


#h1create and fill the histogram
can  = ROOT.TCanvas("can", "histograms", 1400,700)
can2  = ROOT.TCanvas("can2", "histogramss", 1400,700)
can3  = ROOT.TCanvas("can3", "Average Resolution", 1400,700)
can4 = ROOT.TCanvas("can4", "Resolution", 1400,700)
can5 = ROOT.TCanvas("can5", "Resolution hist", 1400,700)
h1 = ROOT.TH1D("h1", "Down dGl", 500, 0.0, 500.0)
h2 = ROOT.TH1D("h2", "Up dGl", 500, 0.0, 500.0)
h3= ROOT.TH1D("h2", "Resolution hist", 200, -1, 1)
entry_down=0
entry_up=0
downdgl_pt=0
updgl_pt=0
k=-1
n=5
inv_Uppt=0
inv_Downpt=0
res=0
xaxis=[]
ressolution=[]
den=np.array([0,0,0,0,0])
sum_resolution=np.array([0.0,0.0,0.0,0.0,0.0])
average_resolution=np.array([0.0,0.0,0.0,0.0,0.0])
pt_bin=np.array([0.005,0.015,0.025,0.035,0.045])

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
            xaxis.append(inv_Uppt)
            ressolution.append(res)
            
            if 0.0<inv_Uppt<pt_bin[0]+0.005:
                den[0]+=1
                sum_resolution[0]+=abs(res)
            
            if (pt_bin[1]-0.005)<inv_Uppt<(pt_bin[1]+0.005):
                den[1]+=1
                sum_resolution[1]+=abs(res)
            
            if (pt_bin[2]-0.005)<inv_Uppt<(pt_bin[2]+0.005):
                den[2]+=1
                sum_resolution[2]+=abs(res)
            if (pt_bin[3]-0.005)<inv_Uppt<(pt_bin[3]+0.005):
                den[3]+=1
                sum_resolution[3]+=abs(res)
            
            if (pt_bin[4]-0.005)<inv_Uppt<(pt_bin[4]+0.005):
                den[4]+=1
                sum_resolution[4]+=abs(res)
            
            
for s in range(5):
    average_resolution[s]= abs(sum_resolution[s])/den[s]
    
print(den, sum_resolution, average_resolution)
can.cd()
h1.Draw()
can.SaveAs("plots/do_ndgl_pt.png")

can2.cd()    
h2.Draw()
can2.SaveAs("plots/up_dgl_pt.png")
can5.cd()    
h3.Draw()
can5.SaveAs("plots/Resolutions_hist.png")


x=np.array(xaxis)
y=np.array(ressolution)
gr = ROOT.TGraph( n, pt_bin, average_resolution )
gr.SetTitle( 'Pt Resolution' )
gr.GetXaxis().SetTitle( '1/pt' )
gr.GetYaxis().SetTitle( 'Average Resolution' )
gr.GetYaxis().SetRangeUser( -0.1,0.1 )
can3.cd()
gr.Draw('PA*')
can3.SaveAs("plots/Average_Resolution.png")

gp = ROOT.TGraph( k, x, y )
gp.SetTitle( 'Pt Resolution' )
gp.GetXaxis().SetTitle( '1/pt' )
gp.GetYaxis().SetTitle( 'Resolution' )
gp.GetYaxis().SetRangeUser( -0.1,0.1 )
can4.cd()
gp.Draw('PA*')
can4.SaveAs("plots/Resolution.png")
    