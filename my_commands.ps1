function create
{
        Param($foldername)
        #Write-Host $foldername
        
        cd C:\Users\ignac_000\proyects\scripts
        python create.py $foldername
        Write-Host "Python script executed--
        Folder and README created, initiated github repo"
        
        cd C:\Users\ignac_000\proyects/$foldername
        
        git init
        git add .
        git commit -m "first commit done by machine"
        git remote add origin https://github.com/ignaciorm/$foldername.git
        git push origin master

        Write-Host "GitHub done" -ForegroundColor Green



        Write-Host "Done" -ForegroundColor Green

}