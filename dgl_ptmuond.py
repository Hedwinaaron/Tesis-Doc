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


#Relevan variables
n=8
sigma=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
average_resolution=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
sigma_hist=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
average_resolution_hist=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
res_error=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
sigma_error=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
bin_size=np.array([5.0,5.0,10.0,15.0,25.0,25.0,75.0,75.0])
empty=np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
#Bining
pt_bin=np.array([35.0,45.0,60.0,85.0,125.0,175.0,275.0,425.0])


#Fitting histograms and extracting mean values, sigma anc correspondng errors
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


#Creating and saving resolutions graphs
gr = ROOT.TGraphErrors( n, pt_bin, average_resolution,bin_size,res_error )
gr.SetTitle( 'Pt Resolution' )
gr.GetXaxis().SetTitle( 'p_{T}\ \mu_{ref}\ [Gev]' )
gr.GetYaxis().SetTitle( 'Mean of 1/p_{T} relative residual' )
gr.GetYaxis().SetRangeUser( -0.015,0.0 )
gr.GetXaxis().SetRangeUser( 0,500)
can.cd()
#can.SetLogx()
gr.Draw('ap')
can.SaveAs("plots/Average_Resolution.png")

gs = ROOT.TGraphErrors( n, pt_bin, sigma,bin_size,sigma_error )
gs.SetTitle( 'Sigma' )
gs.GetXaxis().SetTitle( 'p_{T}\ \mu_{ref}\ [Gev]' )
gs.GetYaxis().SetTitle( 'width of 1/p_{T} relative residual(\sigma)' )
gs.GetYaxis().SetRangeUser( 0.0,0.07 )
gs.GetXaxis().SetRangeUser( 0,500 )
can2.cd()
#can2.SetLogx()
gs.Draw('ap')
can2.SaveAs("plots/Sigma.png")

'''
gp = ROOT.TGraphErrors( n, pt_bin, average_resolution_hist,empty,empty )
gp.SetTitle( 'Pt Resolution' )
gp.GetXaxis().SetTitle( 'Pt' )
gp.GetYaxis().SetTitle( 'Average Resolution' )
gp.GetYaxis().SetRangeUser( -0.06,0.06 )
can3.cd()
can3.SetLogx()
gp.Draw('PA*')
can3.SaveAs("plots/Average_Resolution_histmean.png")


go = ROOT.TGraphErrors( n, pt_bin, sigma_hist,empty,empty )
go.SetTitle( 'Sigma' )
go.GetXaxis().SetTitle( 'Pt' )
go.GetYaxis().SetTitle( 'Standar deviation' )
go.GetYaxis().SetRangeUser( 0.0,0.1 )
can4.cd()
go.Draw('PA*')
can4.SetLogx()
can4.SaveAs("plots/Sigma_hist.png")
'''




    