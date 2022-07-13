#!/usr/bin/python3
import os, sys
import ROOT
import numpy as np
import array as arr

# Open a file
path = "/eos/user/h/hencinas/AOD/TKCosmic_38T_p20-3000/crab_TnP_ntuplizer_muon_Cosmics_Run2018_AOD_TKCosmic/220606_142613/0000/"
files = os.listdir( path )
#create and fill the histogram


h1 = ROOT.TH1D("h1", "Down dGl", 1000, 0.0, 1000.0)
h2 = ROOT.TH1D("h2", "Up dGl", 1000, 0.0, 1000.0)
h3= ROOT.TH1D("h3", "Resolution hist", 200, -1, 1)
h4= ROOT.TH1D("h4", "p_T 30-40", 100, -0.3, 0.3)
h5= ROOT.TH1D("h5", "p_T 40-50", 100, -0.3, 0.3)
h6= ROOT.TH1D("h6", "p_T 50-70 ", 100, -0.3, 0.3)
h7= ROOT.TH1D("h7", "p_T 70-100", 100, -0.3, 0.3)
h8= ROOT.TH1D("h8", "p_T 100-150", 100, -0.3, 0.3)
h9= ROOT.TH1D("h9", "p_T 150-200", 100, -0.3, 0.3)
h10= ROOT.TH1D("h10", "p_T 200-350", 100, -0.3, 0.3)
h11= ROOT.TH1D("h11", "p_T 350-500", 100, -0.3, 0.3)
h32= ROOT.TH1D("h132", "p_T 500-1000", 100, -0.3, 0.3)
h12= ROOT.TH1D("h12", "Up |dz|", 400, 0, 400)
h13= ROOT.TH1D("h13", "Up |dxy|", 400, 0, 120)
h14= ROOT.TH1D("h14", "Down |dz|", 400, 0, 400)
h15= ROOT.TH1D("h15", "Down |dxy|", 400, 0, 120)

h16= ROOT.TH1D("h16", "|dz| 0-5", 100, -0.2, 0.2)
h17= ROOT.TH1D("h17", "|dz| 5-10", 100, -0.2, 0.2)
h18= ROOT.TH1D("h18", "|dz| 10-20", 100, -0.2, 0.2)
h19= ROOT.TH1D("h19", "|dz| 20-30", 100, -0.2, 0.2)
h20= ROOT.TH1D("h20", "|dz| 30-45", 100, -0.2, 0.2)
h21= ROOT.TH1D("h21", "|dz| 45-60", 100, -0.2, 0.2)
h22 =ROOT.TH1D("h22", "|dz| 60-80", 100, -0.2, 0.2)
h23= ROOT.TH1D("h23", "|dz| 80-150", 100, -0.2, 0.2)

h24= ROOT.TH1D("h24", "|dxy| 0-5", 100, -0.2, 0.2)
h25= ROOT.TH1D("h25", "|dxy| 5-10", 100, -0.2, 0.2)
h26= ROOT.TH1D("h26", "|dxy| 10-15", 100, -0.2, 0.2)
h27= ROOT.TH1D("h27", "|dxy| 15-20", 100, -0.2, 0.2)
h28= ROOT.TH1D("h28", "|dxy| 20-30", 100, -0.2, 0.2)
h29= ROOT.TH1D("h29", "|dxy| 30-40", 100, -0.2, 0.2)
h30= ROOT.TH1D("h30", "|dxy| 40-50", 100,-0.2, 0.2)
h31= ROOT.TH1D("h31", "|dxy|  50-80", 100, -0.2, 0.2)



#relevant variables
entry_down=0
entry_up=0
downdgl_pt=0
updgl_pt=0
k=-1
inv_Uppt=0
inv_Downpt=0
res=0
pt_bin=np.array([30,40,50,70,100,150,200,350,500,1000])
dxy_bin=np.array([0,5,10,15,20,30,40,50,80])
dz_bin=np.array([0,5,10,20,30,45,60,80,150])


# This would print all the files and directories
for file in files:
    
    #input the name of the root file
    inFileName = path+"/"+file
    
    #Open root file and get branch
    inFile = ROOT.TFile.Open( inFileName ," READ ")
    tree = inFile.Get ("muon/Events")
    print("Reading from ", inFileName)    
    Entries=tree.GetEntries()
    
    
    
   
    #Events selection and histogram filling
    for i in range(0,Entries):
        tree.GetEntry(i) 
        abstag_eta= abs(tree.tag_eta)
        tag_abseta= abs(tree.tag_eta)
        if tree.HLT_L2Mu10_NoVertex_NoBPTX3BX_v == 1 and tree.tag_pt > 20 and tree.tag_isdGlobal == 1 and tree.tag_phi < -0.6 and tree.tag_phi > -2.6 and abstag_eta < 0.9 and tree.probe_isUpdGlobal: 
            pair_dphi= abs(tree.tag_phi-tree.probe_updgl_phi)
            pair_dphi_reduced= abs(pair_dphi - 3.141592 * (1 + (pair_dphi-3.141592)/abs(pair_dphi-3.141592)))
            #tag_absdxy= abs(tree.tag_dxy)
            #tag_absdz= abs(tree.tag_dz)

            entry_down=i
            downdgl_pt = tree.tag_pt
            down_charge=tree.tag_charge
            down_absdz=abs(tree.tag_dz)
            down_absdxy=abs(tree.tag_dxy) 
    
            if tree.probe_updgl_pt > 30:
                entry_up=i
                updgl_pt = tree.probe_updgl_pt
                up_charge=tree.tag_charge
                up_absdz=abs(tree.probe_updgl_dz)
                up_absdxy=abs(tree.probe_updgl_dxy)
                
        
                
                h12.Fill(up_absdz) 
                h13.Fill(up_absdxy)
                h14.Fill(down_absdz)
                h15.Fill(down_absdxy)
                
                print("Event", i)
                h1.Fill(downdgl_pt)
                
                h2.Fill(updgl_pt)
                
                
                inv_Uppt=up_charge/updgl_pt
                inv_Downpt=down_charge/downdgl_pt
                res=((inv_Uppt)-(inv_Downpt))/(np.sqrt(2)*(inv_Downpt))
                h3.Fill(res)
                k+=1
                print(i,inv_Uppt,inv_Downpt, res)
                
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
                    
                if pt_bin[8]<updgl_pt<pt_bin[9]:
                    h32.Fill(res)   
                #dz bins
                if dz_bin[0]<up_absdz<dz_bin[1]:
                    h16.Fill(res)
                
                if dz_bin[1]<up_absdz<dz_bin[2]:
        
                    h17.Fill(res)
                    
                if dz_bin[2]<up_absdz<dz_bin[3]:
        
                    h18.Fill(res)
                    
                if dz_bin[3]<up_absdz<dz_bin[4]:
        
                    h19.Fill(res)
                
                if dz_bin[4]<up_absdz<dz_bin[5]:
        
                    h20.Fill(res)
                
                if dz_bin[5]<up_absdz<dz_bin[6]:
                    h21.Fill(res)
                
                
                if dz_bin[6]<up_absdz<dz_bin[7]:
                    h22.Fill(res)
                
                
                if dz_bin[7]<up_absdz<dz_bin[8]:
                    h23.Fill(res)    
                
                #dxy bins
                if dxy_bin[0]<up_absdxy<dxy_bin[1]:
                    h24.Fill(res)
                
                if dxy_bin[1]<up_absdxy<dxy_bin[2]:
        
                    h25.Fill(res)
                    
                if dxy_bin[2]<up_absdxy<dxy_bin[3]:
        
                    h26.Fill(res)
                    
                if dxy_bin[3]<up_absdxy<dxy_bin[4]:
        
                    h27.Fill(res)
                
                if dxy_bin[4]<up_absdxy<dxy_bin[5]:
        
                    h28.Fill(res)
                
                if dxy_bin[5]<up_absdxy<dxy_bin[6]:
                    h29.Fill(res)
                
                
                if dxy_bin[6]<up_absdxy<dxy_bin[7]:
                    h30.Fill(res)
                
                
                if dxy_bin[7]<up_absdxy<dxy_bin[8]:
                    h31.Fill(res)
                    

                
        

#creating output root file    
outHistFile = ROOT.TFile.Open ( "Res_hist_MC.root" ,"RECREATE")
outHistFile.cd()

#Hstograms pf pt distribution in upper and lower half
can1  = ROOT.TCanvas("can1", "hist", 800,600)
can1.cd()
h1.Write("down_ndgl_pt")
h1.Draw()
can1.SaveAs("plots/histograms/down_ndgl_pt.png")
can1.Close()

can2 = ROOT.TCanvas("can2", "hist", 800,600)
can2.cd()
h2.Write("up_dgl_pt")
h2.Draw()
can2.SaveAs("plots/histograms/up_dgl_pt.png")
can2.Close()

#histogram of resolution distribution
can3  = ROOT.TCanvas("can3", "hist", 1400,700)
can3.cd()
h3.Write("Resolutions_hist")
h3.Draw()
can3.SaveAs("plots/histograms/Resolutions_hist.png")
can3.Close()

#Histograms of resolution distribution per pt interval 
can4 = ROOT.TCanvas("can4", "hist", 1400,700)
h4.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h4.Write("pt_30-40_hist")
can4.cd()
fit1=h4.Fit("gaus", "S")
h4.Draw()
latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize (0.04)
latex.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit1.Parameter(1),4)))
latex.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit1.Parameter(2),4)))
can4.SaveAs("plots/histograms/pt_30-40_hist.png")
can4.Close()

can5 = ROOT.TCanvas("can5", "hist", 1400,700)
h5.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h5.Write("pt_40-50_hist")
can5.cd()
fit2=h5.Fit("gaus", "S")
h5.Draw()
latex2 = ROOT.TLatex()
latex2.SetNDC()
latex2.SetTextSize (0.04)
latex2.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit2.Parameter(1),4)))
latex2.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit2.Parameter(2),4)))
can5.SaveAs("plots/histograms/pt_40-50_hist.png")
can5.Close()

can6= ROOT.TCanvas("can6", " hist", 1400,700)
h6.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h6.Write("pt_50-70_hist")
can6.cd()
fit3=h6.Fit("gaus", "S")
h6.Draw()
latex3 = ROOT.TLatex()
latex3.SetNDC()
latex3.SetTextSize (0.04)
latex3.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit3.Parameter(1),4)))
latex3.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit3.Parameter(2),4)))
can6.SaveAs("plots/histograms/pt_50-70_hist.png")
can6.Close()

can7= ROOT.TCanvas("can7", "hist", 1400,700)
h7.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h7.Write("pt_70-100_hist")
can7.cd()
fit4=h7.Fit("gaus", "S")
h7.Draw()
latex4 = ROOT.TLatex()
latex4.SetNDC()
latex4.SetTextSize (0.04)
latex4.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit4.Parameter(1),4)))
latex4.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit4.Parameter(2),4)))
can7.SaveAs("plots/histograms/pt_70-100_hist.png")
can7.Close()

can8= ROOT.TCanvas("can8", "hist", 1400,700)
h8.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h8.Write("pt_100-150_hist")
can8.cd()
fit5=h8.Fit("gaus", "S")
h8.Draw()
latex5 = ROOT.TLatex()
latex5.SetNDC()
latex5.SetTextSize (0.04)
latex5.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit5.Parameter(1),4)))
latex5.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit5.Parameter(2),4)))
can8.SaveAs("plots/histograms/pt_100-150_hist.png")
can8.Close()

can9= ROOT.TCanvas("can9", "hist", 1400,700)
h9.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h9.Write("pt_150-200_hist")
can9.cd()
fit6=h9.Fit("gaus", "S")
h9.Draw()
latex6 = ROOT.TLatex()
latex6.SetNDC()
latex6.SetTextSize (0.04)
latex6.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit6.Parameter(1),4)))
latex6.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit6.Parameter(2),4)))
can9.SaveAs("plots/histograms/pt_150-200_hist.png")
can9.Close()

can10= ROOT.TCanvas("can10", "hist", 1400,700)
h10.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h10.Write("pt_200-350_hist")
can10.cd()
fit7=h10.Fit("gaus", "S")
h10.Draw()
latex7 = ROOT.TLatex()
latex7.SetNDC()
latex7.SetTextSize (0.04)
latex7.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit7.Parameter(1),4)))
latex7.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit7.Parameter(2),4)))
can10.SaveAs("plots/histograms/pt_200-350_hist.png")
can10.Close()

can11= ROOT.TCanvas("can11", "hist", 1400,700)
h11.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h11.Write("pt_350-500_hist")
can11.cd()
fit8=h11.Fit("gaus", "S")
h11.Draw()
latex8 = ROOT.TLatex()
latex8.SetNDC()
latex8.SetTextSize (0.04)
latex8.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit8.Parameter(1),4)))
latex8.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit8.Parameter(2),4)))
can11.SaveAs("plots/histograms/pt_350-500_hist.png")
can11.Close()

can36= ROOT.TCanvas("can11", "hist", 1400,700)
h32.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h32.Write("pt_500-1000_hist")
can36.cd()
fit32=h32.Fit("gaus", "S")
h32.Draw()
latex32 = ROOT.TLatex()
latex32.SetNDC()
latex32.SetTextSize (0.04)
latex32.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit32.Parameter(1),4)))
latex32.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit32.Parameter(2),4)))
can36.SaveAs("plots/histograms/pt_350-500_hist.png")
can36.Close()

can12= ROOT.TCanvas("can12", "hist", 1400,700)
can12.cd()
h12.GetXaxis().SetTitle( '|d_z|' )
h12.Write("Up absdz")
h12.Draw()
can12.SaveAs("plots/histograms/Up_absdz.png")
can12.Close()

can13= ROOT.TCanvas("can13", "hist", 1400,700)
can13.cd()
h13.GetXaxis().SetTitle( '|d_xy|' )
h13.Write("Up absdxy")
h13.Draw()
can13.SaveAs("plots/histograms/Up_absdxy.png")
can13.Close()

can14= ROOT.TCanvas("can14", "hist", 1400,700)
can14.cd()
h14.GetXaxis().SetTitle( '|d_z|' )
h14.Write("Down absdz")
h14.Draw()
can14.SaveAs("plots/histograms/Down_absdz.png")
can14.Close()

can15= ROOT.TCanvas("can15", "hist", 1400,700)
can15.cd()
h15.GetXaxis().SetTitle( '|d_xy|' )
h15.Write("Up absdxy")
h15.Draw()
can15.SaveAs("plots/histograms/Down_absdxy.png")
can15.Close()

#Histograms of resolution distribution per |dz| interval 
can16= ROOT.TCanvas("can16", "hist", 1400,700)
h16.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h16.Write("|dz|_0-5_hist")
can16.cd()
fit9=h16.Fit("gaus", "S")
h16.Draw()
latex9 = ROOT.TLatex()
latex9.SetNDC()
latex9.SetTextSize (0.04)
latex9.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit1.Parameter(1),4)))
latex9.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit1.Parameter(2),4)))
can16.SaveAs("plots/histograms/dz_0-5_hist.png")
can16.Close()

can17= ROOT.TCanvas("can17", "hist", 1400,700)
h17.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h17.Write("|dz|_5-10_hist")
can17.cd()
fit10=h17.Fit("gaus", "S")
h17.Draw()
latex10 = ROOT.TLatex()
latex10.SetNDC()
latex10.SetTextSize (0.04)
latex10.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit2.Parameter(1),4)))
latex10.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit2.Parameter(2),4)))
can17.SaveAs("plots/histograms/dz_5-10_hist.png")
can17.Close()

can18= ROOT.TCanvas("can18", "hist", 1400,700)
h18.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h18.Write("|dz|_10-20_hist")
can18.cd()
fit11=h18.Fit("gaus", "S")
h18.Draw()
latex11 = ROOT.TLatex()
latex11.SetNDC()
latex11.SetTextSize (0.04)
latex11.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit3.Parameter(1),4)))
latex11.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit3.Parameter(2),4)))
can18.SaveAs("plots/histograms/dz_10-20_hist.png")
can18.Close()

can19= ROOT.TCanvas("can19", "hist", 1400,700)
h19.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h19.Write("|dz|_20-30_hist")
can19.cd()
fit12=h19.Fit("gaus", "S")
h19.Draw()
latex12 = ROOT.TLatex()
latex12.SetNDC()
latex12.SetTextSize (0.04)
latex12.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit4.Parameter(1),4)))
latex12.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit4.Parameter(2),4)))
can19.SaveAs("plots/histograms/dz_20-30_hist.png")
can19.Close()

can20= ROOT.TCanvas("can20", "hist", 1400,700)
h20.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h20.Write("|dz|_30-45_hist")
can20.cd()
fit13=h20.Fit("gaus", "S")
h20.Draw()
latex13 = ROOT.TLatex()
latex13.SetNDC()
latex13.SetTextSize (0.04)
latex13.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit5.Parameter(1),4)))
latex13.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit5.Parameter(2),4)))
can20.SaveAs("plots/histograms/dz_30-45_hist.png")
can20.Close()

can21= ROOT.TCanvas("can21", "hist", 1400,700)
h21.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h21.Write("|dz|_45-60_hist")
can21.cd()
fit14=h21.Fit("gaus", "S")
h21.Draw()
latex14 = ROOT.TLatex()
latex14.SetNDC()
latex14.SetTextSize (0.04)
latex14.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit6.Parameter(1),4)))
latex14.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit6.Parameter(2),4)))
can21.SaveAs("plots/histograms/dz_45-60_hist.png")
can21.Close()

can22= ROOT.TCanvas("can22", "hist", 1400,700)
h22.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h22.Write("|dz|_60-80_hist")
can22.cd()
fit15=h22.Fit("gaus", "S")
h22.Draw()
latex15 = ROOT.TLatex()
latex15.SetNDC()
latex15.SetTextSize (0.04)
latex15.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit7.Parameter(1),4)))
latex15.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit7.Parameter(2),4)))
can22.SaveAs("plots/histograms/dz_60-80_hist.png")
can22.Close()

can23= ROOT.TCanvas("can23", "hist", 1400,700)
h23.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h23.Write("|dz|_80-400_hist")
can23.cd()
fit16=h23.Fit("gaus", "S")
h23.Draw()
latex16 = ROOT.TLatex()
latex16.SetNDC()
latex16.SetTextSize (0.04)
latex16.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit8.Parameter(1),4)))
latex16.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit8.Parameter(2),4)))
can23.SaveAs("plots/histograms/dz_80-150_hist.png")
can23.Close()


#Histograms of resolution distribution per |dxy| interval 
can24= ROOT.TCanvas("can24", "hist", 1400,700)
h24.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h24.Write("|dxy|_0-5_hist")
can24.cd()
fit17=h24.Fit("gaus", "S")
h24.Draw()
latex17 = ROOT.TLatex()
latex17.SetNDC()
latex17.SetTextSize (0.04)
latex17.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit1.Parameter(1),4)))
latex17.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit1.Parameter(2),4)))
can24.SaveAs("plots/histograms/dxy_0-5_hist.png")
can24.Close()

can25= ROOT.TCanvas("can25", "hist", 1400,700)
h25.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h25.Write("|dxy|_5-10_hist")
can25.cd()
fit18=h25.Fit("gaus", "S")
h25.Draw()
latex18 = ROOT.TLatex()
latex18.SetNDC()
latex18.SetTextSize (0.04)
latex18.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit2.Parameter(1),4)))
latex18.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit2.Parameter(2),4)))
can25.SaveAs("plots/histograms/dxy_5-10_hist.png")
can25.Close()

can26= ROOT.TCanvas("can26", "hist", 1400,700)
h26.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h26.Write("|dxy|_10-15_hist")
can26.cd()
fit19=h26.Fit("gaus", "S")
h26.Draw()
latex19 = ROOT.TLatex()
latex19.SetNDC()
latex19.SetTextSize (0.04)
latex19.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit3.Parameter(1),4)))
latex19.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit3.Parameter(2),4)))
can26.SaveAs("plots/histograms/dxy_10-15_hist.png")
can26.Close()

can27= ROOT.TCanvas("can27", "hist", 1400,700)
h27.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h27.Write("|dxy|_15-20_hist")
can27.cd()
fit20=h27.Fit("gaus", "S")
h27.Draw()
latex20 = ROOT.TLatex()
latex20.SetNDC()
latex20.SetTextSize (0.04)
latex20.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit4.Parameter(1),4)))
latex20.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit4.Parameter(2),4)))
can27.SaveAs("plots/histograms/dxy_15-20_hist.png")
can27.Close()

can28= ROOT.TCanvas("can28", "hist", 1400,700)
h28.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h28.Write("|dxy|_20-30_hist")
can28.cd()
fit21=h28.Fit("gaus", "S")
h28.Draw()
latex21= ROOT.TLatex()
latex21.SetNDC()
latex21.SetTextSize (0.04)
latex21.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit5.Parameter(1),4)))
latex21.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit5.Parameter(2),4)))
can28.SaveAs("plots/histograms/dxy_20-30_hist.png")
can28.Close()

can29= ROOT.TCanvas("can29", "hist", 1400,700)
h29.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h29.Write("|dxy|_30-40_hist")
can29.cd()
fit22=h29.Fit("gaus", "S")
h29.Draw()
latex22 = ROOT.TLatex()
latex22.SetNDC()
latex22.SetTextSize (0.04)
latex22.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit6.Parameter(1),4)))
latex22.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit6.Parameter(2),4)))
can29.SaveAs("plots/histograms/dxy_30-40_hist.png")
can29.Close()

can30= ROOT.TCanvas("can30", "hist", 1400,700)
h30.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h30.Write("|dxy|_40-50_hist")
can30.cd()
fit23=h30.Fit("gaus", "S")
h30.Draw()
latex23 = ROOT.TLatex()
latex23.SetNDC()
latex23.SetTextSize (0.04)
latex23.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit7.Parameter(1),4)))
latex23.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit7.Parameter(2),4)))
can30.SaveAs("plots/histograms/dxy_40-50_hist.png")
can30.Close()

can31= ROOT.TCanvas("can31", "hist", 1400,700)
h31.GetXaxis().SetTitle( 'q/p_{T} relative residual' )
h31.Write("|dxy|_50-100_hist")
can31.cd()
fit24=h31.Fit("gaus", "S")
h31.Draw()
latex24 = ROOT.TLatex()
latex24.SetNDC()
latex24.SetTextSize (0.04)
latex24.DrawText (0.7 ,0.5, "Fit mean= "+str(round(fit8.Parameter(1),4)))
latex24.DrawText (0.7 ,0.45, "Fit Std Dev = "+str(round(fit8.Parameter(2),4)))
can31.SaveAs("plots/histograms/dxy_50-80_hist.png")
can31.Close()


#closing output file
outHistFile.Close()