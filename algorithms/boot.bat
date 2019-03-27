@ECHO OFF
rem add Ubuntu EFI entry

bcdedit /enum firmware

for /f "tokens=2 delims={}" %%a in ('bcdedit /copy {bootmgr} /d "Ubuntu Secure Boot"') do set guid={%%a}
bcdedit /set %guid% path \EFI\ubuntu\shimx64.efi
bcdedit /set {fwbootmgr} displayorder %guid% /addfirst

bcdedit /enum firmware
pause