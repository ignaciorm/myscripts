function create
{
        Param($foldername)
        #Write-Host $foldername
        
        cd C:\Users\Ignacio\Proyects\myscripts
        python create.py $foldername
        Write-Host "Python script executed--
        Folder and README created, initiated github repo"
        
        cd C:\Users\Ignacio\Proyects/$foldername
        
        git init
        git add .
        git commit -m "first commit done by machine"
        git remote add origin https://github.com/ignaciorm/$foldername.git
        git push origin master

        Write-Host "GitHub done" -ForegroundColor Green



        Write-Host "Done" -ForegroundColor Green

}