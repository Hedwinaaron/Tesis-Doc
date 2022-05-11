import ROOT
import numpy as np
import math 
import array as arr
import sys

if len( sys.argv ) != 2:
  print("USAGE: %s <input file >"%( sys.argv [0]))
  sys.exit (1)
 #input the name of the root file
inFileName = sys.argv[1]

#Open root file and get branch
inFile = ROOT.TFile.Open( inFileName ," READ ")
print("Reading from ", inFileName)      

can  = ROOT.TCanvas("can", "histograms", 1400,700)
can2  = ROOT.TCanvas("can2", "histograms", 1400,700)
can3  = ROOT.TCanvas("can3", "histograms", 1400,700)
can4  = ROOT.TCanvas("can4", "histograms", 1400,700)
can5  = ROOT.TCanvas("can5", "histograms", 1400,700)
can6  = ROOT.TCanvas("can6", "histograms", 1400,700)


#Relevan variables
n=8
sigma=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
average_resolution=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
sigma_dz=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
average_resolution_dz=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
sigma_dxy=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
average_resolution_dxy=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
sigma_hist=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
average_resolution_hist=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
res_error=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
sigma_error=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
mean_error_dz=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
sigma_error_dz=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
mean_error_dxy=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
sigma_error_dxy=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
bin_size=np.array([5.0,5.0,10.0,15.0,25.0,25.0,75.0,75.0])

bin_size_dz=np.array([2.5,2.5,5,5,7.5,7.5,10,160])
bin_size_dxy=np.array([2.5,2.5,2.5,2.5,5,5,5,25])

empty=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
#Bining
pt_bin=np.array([35.0,45.0,60.0,85.0,125.0,175.0,275.0,425.0])
dz_bin=np.array([2.5,7.5,15,25.0,37.5,52.5,70,240.0])
dxy_bin=np.array([2.5,7.5,12.5,17.5,25.0,35.0,45.0,75.0])
#Fitting histograms and extracting mean values, sigma and correspondng errors for p_T bins
h1=inFile.Get("pt_30-40_hist")
fit1= h1.Fit("gaus", "S")
mean_res1=fit1.Parameter(1)
sigma1=fit1.Parameter(2)
res_error[0]=fit1.ParError(1)
sigma_error[0]=fit1.ParError(2)
average_resolution[0]=mean_res1
sigma[0]=sigma1
sigma_hist[0]=h1.GetStdDev()
average_resolution_hist[0]=h1.GetMean()


h2=inFile.Get("pt_40-50_hist")
fit2= h2.Fit("gaus", "S")
mean_res2=fit2.Parameter(1)
sigma2=fit2.Parameter(2)
res_error[1]=fit2.ParError(1)
sigma_error[1]=fit2.ParError(2)
average_resolution[1]=mean_res2
sigma[1]=sigma2
sigma_hist[1]=h2.GetStdDev()
average_resolution_hist[1]=h2.GetMean()

h3=inFile.Get("pt_50-70_hist")
fit3= h3.Fit("gaus", "S")
mean_res3=fit3.Parameter(1)
sigma3=fit3.Parameter(2)
res_error[2]=fit3.ParError(1)
sigma_error[2]=fit3.ParError(2)
average_resolution[2]=mean_res3
sigma[2]=sigma3
sigma_hist[2]=h3.GetStdDev()
average_resolution_hist[2]=h3.GetMean()

h4=inFile.Get("pt_70-100_hist")
fit4= h4.Fit("gaus", "S")
mean_res4=fit4.Parameter(1)
sigma4=fit4.Parameter(2)
res_error[3]=fit4.ParError(1)
sigma_error[3]=fit4.ParError(2)
average_resolution[3]=mean_res4
sigma[3]=sigma4
sigma_hist[3]=h4.GetStdDev()
average_resolution_hist[3]=h4.GetMean()

h5=inFile.Get("pt_100-150_hist")
fit5= h5.Fit("gaus", "S")
mean_res5=fit5.Parameter(1)
sigma5=fit5.Parameter(2)
res_error[4]=fit5.ParError(1)
sigma_error[4]=fit5.ParError(2)
average_resolution[4]=mean_res5
sigma[4]=sigma5
sigma_hist[4]=h5.GetStdDev()
average_resolution_hist[4]=h5.GetMean()

h6=inFile.Get("pt_150-200_hist")
fit6= h6.Fit("gaus", "S")
mean_res6=fit6.Parameter(1)
sigma6=fit6.Parameter(2)
res_error[5]=fit6.ParError(1)
sigma_error[5]=fit6.ParError(2)
average_resolution[5]=mean_res6
sigma[5]=sigma6
sigma_hist[5]=h6.GetStdDev()
average_resolution_hist[5]=h6.GetMean()

h7=inFile.Get("pt_200-350_hist")
fit7= h7.Fit("gaus", "S")
mean_res7=fit7.Parameter(1)
sigma7=fit7.Parameter(2)
res_error[6]=fit7.ParError(1)
sigma_error[6]=fit7.ParError(2)
average_resolution[6]=mean_res7
sigma[6]=sigma7
sigma_hist[6]=h7.GetStdDev()
average_resolution_hist[6]=h7.GetMean()

h8=inFile.Get("pt_350-500_hist")
fit8= h8.Fit("gaus", "S")
mean_res8=fit8.Parameter(1)
sigma8=fit8.Parameter(2)
res_error[7]=fit8.ParError(1)
sigma_error[7]=fit8.ParError(2)
average_resolution[7]=mean_res8
sigma[7]=sigma8
sigma_hist[7]=h8.GetStdDev()
average_resolution_hist[7]=h8.GetMean()

#Fitting histograms and extracting mean values, sigma and correspondng errors for d_z bins
h9=inFile.Get("|dz|_0-5_hist")
fit9= h9.Fit("gaus", "S")
mean_res9=fit9.Parameter(1)
sigma9=fit9.Parameter(2)
mean_error_dz[0]=fit9.ParError(1)
sigma_error_dz[0]=fit9.ParError(2)
average_resolution_dz[0]=mean_res9
sigma_dz[0]=sigma9


h10=inFile.Get("|dz|_5-10_hist")
fit10= h10.Fit("gaus", "S")
mean_res10=fit10.Parameter(1)
sigma10=fit10.Parameter(2)
mean_error_dz[1]=fit10.ParError(1)
sigma_error_dz[1]=fit10.ParError(2)
average_resolution_dz[1]=mean_res10
sigma_dz[1]=sigma10

h11=inFile.Get("|dz|_10-20_hist")
fit11= h11.Fit("gaus", "S")
mean_res11=fit11.Parameter(1)
sigma11=fit11.Parameter(2)
mean_error_dz[2]=fit11.ParError(1)
sigma_error_dz[2]=fit11.ParError(2)
average_resolution_dz[2]=mean_res11
sigma_dz[2]=sigma11


h12=inFile.Get("|dz|_20-30_hist")
fit12= h12.Fit("gaus", "S")
mean_res12=fit12.Parameter(1)
sigma12=fit12.Parameter(2)
mean_error_dz[3]=fit12.ParError(1)
sigma_error_dz[3]=fit12.ParError(2)
average_resolution_dz[3]=mean_res12
sigma_dz[3]=sigma12


h13=inFile.Get("|dz|_30-45_hist")
fit13= h13.Fit("gaus", "S")
mean_res13=fit13.Parameter(1)
sigma13=fit13.Parameter(2)
mean_error_dz[4]=fit13.ParError(1)
sigma_error_dz[4]=fit13.ParError(2)
average_resolution_dz[4]=mean_res13
sigma_dz[4]=sigma13


h14=inFile.Get("|dz|_45-60_hist")
fit14= h14.Fit("gaus", "S")
mean_res14=fit14.Parameter(1)
sigma14=fit14.Parameter(2)
mean_error_dz[5]=fit14.ParError(1)
sigma_error_dz[5]=fit14.ParError(2)
average_resolution_dz[5]=mean_res14
sigma_dz[5]=sigma14

h15=inFile.Get("|dz|_60-80_hist")
fit15= h15.Fit("gaus", "S")
mean_res15=fit15.Parameter(1)
sigma15=fit15.Parameter(2)
mean_error_dz[6]=fit15.ParError(1)
sigma_error_dz[6]=fit15.ParError(2)
average_resolution_dz[6]=mean_res15
sigma_dz[6]=sigma15

h16=inFile.Get("|dz|_80-400_hist")
fit16= h16.Fit("gaus", "S")
mean_res16=fit16.Parameter(1)
sigma16=fit16.Parameter(2)
mean_error_dz[7]=fit16.ParError(1)
sigma_error_dz[7]=fit16.ParError(2)
average_resolution_dz[7]=mean_res16
sigma_dz[7]=sigma16



#Fitting histograms and extracting mean values, sigma and correspondng errors for d_xy bins
h17=inFile.Get("|dxy|_0-5_hist")
fit17= h17.Fit("gaus", "S")
mean_res17=fit17.Parameter(1)
sigma17=fit17.Parameter(2)
mean_error_dxy[0]=fit17.ParError(1)
sigma_error_dxy[0]=fit17.ParError(2)
average_resolution_dxy[0]=mean_res17
sigma_dxy[0]=sigma17


h18=inFile.Get("|dxy|_5-10_hist")
fit18= h18.Fit("gaus", "S")
mean_res18=fit18.Parameter(1)
sigma18=fit18.Parameter(2)
mean_error_dxy[1]=fit18.ParError(1)
sigma_error_dxy[1]=fit18.ParError(2)
average_resolution_dxy[1]=mean_res18
sigma_dxy[1]=sigma18

h19=inFile.Get("|dxy|_10-15_hist")
fit19= h19.Fit("gaus", "S")
mean_res19=fit19.Parameter(1)
sigma19=fit19.Parameter(2)
mean_error_dxy[2]=fit19.ParError(1)
sigma_error_dxy[2]=fit19.ParError(2)
average_resolution_dxy[2]=mean_res19
sigma_dxy[2]=sigma19


h20=inFile.Get("|dxy|_15-20_hist")
fit20= h20.Fit("gaus", "S")
mean_res20=fit20.Parameter(1)
sigma20=fit20.Parameter(2)
mean_error_dxy[3]=fit20.ParError(1)
sigma_error_dxy[3]=fit20.ParError(2)
average_resolution_dxy[3]=mean_res20
sigma_dxy[3]=sigma20



h21=inFile.Get("|dxy|_20-30_hist")
fit21= h21.Fit("gaus", "S")
mean_res21=fit21.Parameter(1)
sigma21=fit21.Parameter(2)
mean_error_dxy[4]=fit21.ParError(1)
sigma_error_dxy[4]=fit21.ParError(2)
average_resolution_dxy[4]=mean_res21
sigma_dxy[4]=sigma21



h22=inFile.Get("|dxy|_30-40_hist")
fit22= h22.Fit("gaus", "S")
mean_res22=fit22.Parameter(1)
sigma22=fit22.Parameter(2)
mean_error_dxy[5]=fit22.ParError(1)
sigma_error_dxy[5]=fit22.ParError(2)
average_resolution_dxy[5]=mean_res22
sigma_dxy[5]=sigma22


h23=inFile.Get("|dxy|_40-50_hist")
fit23= h23.Fit("gaus", "S")
mean_res23=fit23.Parameter(1)
sigma23=fit23.Parameter(2)
mean_error_dxy[6]=fit23.ParError(1)
sigma_error_dxy[6]=fit23.ParError(2)
average_resolution_dxy[6]=mean_res23
sigma_dxy[6]=sigma23

h24=inFile.Get("|dxy|_50-100_hist")
fit24= h24.Fit("gaus", "S")
mean_res24=fit24.Parameter(1)
sigma24=fit24.Parameter(2)
mean_error_dxy[7]=fit24.ParError(1)
sigma_error_dxy[7]=fit24.ParError(2)
average_resolution_dxy[7]=mean_res24
sigma_dxy[7]=sigma24


#Creating and saving resolutions graphs
gr = ROOT.TGraphErrors( n, pt_bin, average_resolution,bin_size,res_error )
gr.SetTitle( 'Pt Resolution' )
gr.GetXaxis().SetTitle( 'p_{T}\ \mu_{ref}\ [GeV]' )
gr.GetYaxis().SetTitle( 'Mean of q/p_{T} relative residual' )
gr.GetYaxis().SetRangeUser( -0.015,0.0 )
gr.GetXaxis().SetRangeUser( 0,500)
can.cd()
can.SetGrid()
#can.SetLogx()
gr.Draw('ap')
can.SaveAs("plots/Average_Resolution.png")

gs = ROOT.TGraphErrors( n, pt_bin, sigma,bin_size,sigma_error )
gs.SetTitle( 'Sigma' )
gs.GetXaxis().SetTitle( 'p_{T}\ \mu_{ref}\ [GeV]' )
gs.GetYaxis().SetTitle( 'width of q/p_{T} relative residual' )
gs.GetYaxis().SetRangeUser( 0.0,0.07 )
gs.GetXaxis().SetRangeUser( 0,500 )
can2.cd()
can2.SetGrid()
#can2.SetLogx()
gs.Draw('ap')
can2.SaveAs("plots/Sigma.png")


gz = ROOT.TGraphErrors( n, dz_bin, average_resolution_dz,bin_size_dz,mean_error_dz )
gz.SetTitle( 'Resolution' )
gz.GetXaxis().SetTitle( '|dz|' )
gz.GetYaxis().SetTitle( 'Mean of q/p_{T} relative residual' )
can3.cd()
can3.SetGrid()
gz.Draw('ap')
can3.SaveAs("plots/Average_Resolution_|dz|.png")

gz1 = ROOT.TGraphErrors( n, dz_bin, sigma_dz,bin_size_dz,sigma_error_dz )
gz1.SetTitle( 'Sigma' )
gz1.GetXaxis().SetTitle( '|dz|' )
gz1.GetYaxis().SetTitle( 'width of q/p_{T} relative residual' )
can4.cd()
can4.SetGrid()
gz1.Draw('ap')
can4.SaveAs("plots/Sigma_dz.png")


gdxy = ROOT.TGraphErrors( n, dxy_bin, average_resolution_dxy,bin_size_dxy,mean_error_dxy )
gdxy.SetTitle( 'Resolution' )
gdxy.GetXaxis().SetTitle( '|dxy|' )
gdxy.GetYaxis().SetTitle( 'Mean of q/p_{T} relative residual' )
can5.cd()
can5.SetGrid()
gdxy.Draw('ap')
can5.SaveAs("plots/Average_Resolution_|dxy|.png")

gdxy1 = ROOT.TGraphErrors( n, dxy_bin, sigma_dxy,bin_size_dxy,sigma_error_dxy )
gdxy1.SetTitle( 'Sigma' )
gdxy1.GetXaxis().SetTitle( '|dxy|' )
gdxy1.GetYaxis().SetTitle( 'width of q/p_{T} relative residual' )
can6.cd()
can6.SetGrid()
gdxy1.Draw('ap')
can6.SaveAs("plots/Sigma_dxy.png")





    