function test
{
        Param($foldername)
        #Write-Host $name
        
        cd C:\Users\ignac_000\proyects\scripts
        python create.py $foldername
        Write-Host "Python script executed"
        cd C:\Users\ignac_000\proyects

        Write-Host "Done" -ForegroundColor Green

}