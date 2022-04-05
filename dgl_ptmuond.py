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
can6= ROOT.TCanvas("can6", "Pt hist", 1400,700)
can7= ROOT.TCanvas("can7", "Pt hist", 1400,700)
can8= ROOT.TCanvas("can8", "Pt hist", 1400,700)
can9= ROOT.TCanvas("can9", "Pt hist", 1400,700)
can10= ROOT.TCanvas("can10", "Pt hist", 1400,700)
can11= ROOT.TCanvas("can11", "Sigma", 1400,700)
h1 = ROOT.TH1D("h1", "Down dGl", 500, 0.0, 500.0)
h2 = ROOT.TH1D("h2", "Up dGl", 500, 0.0, 500.0)
h3= ROOT.TH1D("h3", "Resolution hist", 200, -1, 1)
h4= ROOT.TH1D("h4", "Res Pt_0-100 hist ", 100, -0.1, 0.1)
h5= ROOT.TH1D("h5", "Res Pt_100-200 hist ", 100, -0.1, 0.1)
h6= ROOT.TH1D("h6", "Res Pt_200-300 hist ", 100, -0.1, 0.1)
h7= ROOT.TH1D("h7", "Res Pt_300-400 hist ", 100, -0.1, 0.1)
h8= ROOT.TH1D("h8", "Res Pt_400-500 hist ", 100, -0.1, 0.1)

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
empty=np.array([0.0,0.0,0.0,0.0,0.0])
sum_resolution=np.array([0.0,0.0,0.0,0.0,0.0])
sigma=np.array([0.0,0.0,0.0,0.0,0.0])
average_resolution=np.array([0.0,0.0,0.0,0.0,0.0])
average_resolution1=np.array([0.0,0.0,0.0,0.0,0.0])
res_error=np.array([0.0,0.0,0.0,0.0,0.0])
sigma_error=np.array([0.0,0.0,0.0,0.0,0.0])
pt_bin=np.array([50.0,150.0,250.0,350.0,450.0])

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
            
            if 0.0<updgl_pt<pt_bin[0]+50.0:
                den[0]+=1
                sum_resolution[0]+=res
                h4.Fill(res)
            
            if (pt_bin[1]-50.0)<updgl_pt<(pt_bin[1]+50.0):
                den[1]+=1
                sum_resolution[1]+=res
                h5.Fill(res)
                
            if (pt_bin[2]-50.0)<updgl_pt<(pt_bin[2]+50.0):
                den[2]+=1
                sum_resolution[2]+=res
                h6.Fill(res)
                
            if (pt_bin[3]-50.0)<updgl_pt<(pt_bin[3]+50.0):
                den[3]+=1
                sum_resolution[3]+=res
                h7.Fill(res)
            
            if (pt_bin[4]-50.0)<updgl_pt<(pt_bin[4]+50.0):
                den[4]+=1
                sum_resolution[4]+=res
                h8.Fill(res)
                
                
for s in range(5):
    average_resolution1[s]= abs(sum_resolution[s])/den[s]
    
            
            
can.cd()
h1.Draw()
can.SaveAs("plots/do_ndgl_pt.png")

can2.cd()    
h2.Draw()
can2.SaveAs("plots/up_dgl_pt.png")

can5.cd()    
h3.Draw()
can5.SaveAs("plots/Resolutions_hist.png")

can6.cd()
fit1= h4.Fit("gaus", "S")
mean_res1=fit1.Parameter(1)
sigma1=fit1.Parameter(2)
res_error[0]=fit1.ParError(1)
sigma_error[0]=fit1.ParError(2)
print("1",mean_res1,sigma1)
average_resolution[0]=mean_res1
sigma[0]=sigma1
h4.Draw()
can6.SaveAs("plots/pt_0-100_hist.png")

can7.cd()
fit2= h5.Fit("gaus", "S")
mean_res2=fit2.Parameter(1)
sigma2=fit2.Parameter(2)
res_error[1]=fit2.ParError(1)
sigma_error[1]=fit2.ParError(2)
print("2",mean_res2, sigma2)
average_resolution[1]=mean_res2
sigma[1]=sigma2
h5.Draw()
can7.SaveAs("plots/pt_100-200_hist.png")

can8.cd()
fit3= h6.Fit("gaus", "S")
mean_res3=fit3.Parameter(1)
sigma3=fit3.Parameter(2)
res_error[2]=fit3.ParError(1)
sigma_error[2]=fit3.ParError(2)
print("3",mean_res3, sigma3)
average_resolution[2]=mean_res3
sigma[2]=sigma3
h6.Draw()
can8.SaveAs("plots/pt_200-300_hist.png")

can9.cd()
fit4= h7.Fit("gaus", "S")
mean_res4=fit4.Parameter(1)
sigma4=fit4.Parameter(2)
res_error[3]=fit4.ParError(1)
sigma_error[3]=fit4.ParError(2)
print("4",mean_res4, sigma4)
average_resolution[3]=mean_res4
sigma[3]=sigma4
h7.Draw()
can9.SaveAs("plots/pt_300-400_hist.png")

can10.cd()
fit5= h8.Fit("gaus", "S")
mean_res5=fit5.Parameter(1)
sigma5=fit5.Parameter(2)
res_error[4]=fit5.ParError(1)
sigma_error[4]=fit5.ParError(2)
print("5",mean_res5, sigma5,res_error,sigma_error)
average_resolution[4]=mean_res5
sigma[4]=sigma5
h8.Draw()
can10.SaveAs("plots/pt_400-500_hist.png")
print(average_resolution)


MU=ROOT.TMultiGraph()
gu = ROOT.TGraph( n, pt_bin, average_resolution1, )
gu.SetMarkerColor( 4 )
MU.Add(gu)
gr = ROOT.TGraphErrors( n, pt_bin, average_resolution,empty,res_error )
MU.Add(gr)
MU.SetTitle( 'Pt Resolution' )
MU.GetXaxis().SetTitle( 'pt' )
MU.GetYaxis().SetTitle( 'Average Resolution' )
MU.GetYaxis().SetRangeUser( -0.3,0.1 )
legend = ROOT.TLegend(.73,.92,.97,.73);
legend.AddEntry(gu,"Average resolution","lep");
legend.AddEntry(gr," Gaus Fit mean","lep");
can3.cd()
MU.Draw('PA*')
legend.Draw()
can3.SaveAs("plots/Average_Resolution.png")


x=np.array(xaxis)
y=np.array(ressolution)
gp = ROOT.TGraph( k, x, y )
gp.SetTitle( 'Pt Resolution' )
gp.GetXaxis().SetTitle( '1/pt' )
gp.GetYaxis().SetTitle( 'Resolution' )
gp.GetYaxis().SetRangeUser( -0.1,0.1 )
can4.cd()
gp.Draw('PA*')
can4.SaveAs("plots/Resolution.png")

gs = ROOT.TGraphErrors( n, pt_bin, sigma,empty,sigma_error )
gs.SetTitle( 'Sigma' )
gs.GetXaxis().SetTitle( 'pt' )
gs.GetYaxis().SetTitle( 'Standar deviation' )
gs.GetYaxis().SetRangeUser( 0.0,0.3 )
can11.cd()
gs.Draw('PA*')
can11.SaveAs("plots/Sigma.png")
    