param($output="scripts.rpa") 
$fullList = ""

$files = Get-ChildItem "." -filter "*.rpyc"

foreach ($f in $files){
    $fullList += $f.name + " " 
}

Invoke-Expression -Command "python rpatool -c $output $fullList"

Write-Output "done"