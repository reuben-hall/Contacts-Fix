$contacts = Import-Csv -Path './Contacts Fix/contacts-2.csv'

$lineCount = 0
foreach ($contact in $contacts) {
    Write-Host $contact."Mobile Phone"
    $lineCount++
}

Write-Host "Processed $lineCount items"