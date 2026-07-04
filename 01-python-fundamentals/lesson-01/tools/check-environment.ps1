$ErrorActionPreference = "Stop"

Write-Host "Lesson 1 environment check"
Write-Host "Workspace: $(Resolve-Path ..\..)"

$launchers = @("python", "py", "python3")
$workingLauncher = $null

foreach ($launcher in $launchers) {
    $command = Get-Command $launcher -ErrorAction SilentlyContinue
    if ($null -eq $command) {
        Write-Host "${launcher}: not found"
        continue
    }

    try {
        $versionOutput = & $launcher --version 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Host "${launcher}: $versionOutput"
            $workingLauncher = $launcher
            break
        }
        Write-Host "${launcher}: failed with exit code $LASTEXITCODE"
    }
    catch {
        Write-Host "${launcher}: found at $($command.Source), but did not launch"
    }
}

if ($null -eq $workingLauncher) {
    Write-Error "No working Python launcher found. Install or repair Python 3.11+ before continuing."
}

Write-Host "Use this command from the lesson folder:"
Write-Host "$workingLauncher -m unittest discover -s tests -v"
