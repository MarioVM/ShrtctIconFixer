# run_iconfxr.ps1
# PowerShell script to run the iconfxr.py Python script

# Function to check if the console is elevated
function Test-IsAdmin {
  $currentUser = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
  $currentUser.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

# Ensure the script is being run in the same directory as iconfxr.py
$scriptDir = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent
Set-Location $scriptDir

# Check if the console is elevated
if (-not (Test-IsAdmin)) {
  Write-Host "This script needs to be run as an administrator. Please run the console as an administrator and try again." -ForegroundColor Red
  exit 1
}

# Check if Python is installed
$pythonExists = Get-Command python -ErrorAction SilentlyContinue

if (-not $pythonExists) {
  Write-Host "Python is not installed. Please install Python before running this script." -ForegroundColor Red
  exit 1
}

# Check if the required Python packages are installed
$requiredPackages = @("pywin32", "tqdm")
foreach ($package in $requiredPackages) {
  try {
      pip show $package | Out-Null
  } catch {
      Write-Host "The Python package '$package' is not installed. Installing now..."
      pip install $package
  }
}

# Run the iconfxr.py script
Write-Host "Running iconfxr.py script..."
python iconfxr.py
