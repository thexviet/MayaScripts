string $openWindows[] = `lsUI -windows`;

for ($i=0; $i < size ($openWindows);$i++) 
{ 
if ($openWindows[$i] != "MayaWindow" && $openWindows[$i] != "scriptEditorPanel1Window") 
{ 
deleteUI $openWindows[$i]; 
windowPref -remove $openWindows[$i]; 
}
}
