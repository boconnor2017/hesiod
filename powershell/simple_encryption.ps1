# Simple Encryption Algorithm
# Author: Brendan O'Connor
# Date: August 2023

# Capture input from command line 
param(
[string]$a
)

# Functions
Function EncryptVal {
[cmdletbinding()]
    Param (
       [String]$ecs, [String]$edv, [String]$ede
    )

    #Encryption Keys
    $baseCharSet = "a b c d e f g h i j k l m n o p q r s t u v w x y z . , / : - + = 1 2 3 4 5 6 7 8 9 0"
    $encCharSet01 = "0 9 8 7 6 5 4 3 2 1 + - = / : a b c d e f g h i j k l m n o p q r s t u v w x y z . ,"

    #Parameters
    $baseCharVal = $baseCharSet.Split(" ")
    $encCharVal01 = $encCharSet01.Split(" ")
    $paramCharVal = $edv.ToCharArray()
    $encResult = ""
    $z = ""
    $i = 0
    $n = 0


    if($ede -eq "E") {
        #Match each character to associated encryption key
        foreach ($char in $paramCharVal) {
            foreach ($base in $baseCharVal){
                if($base -eq $char){
                    $encResult = $encResult+$encCharVal01[$i]  
                }
                $i = $i+1
            }
            $i = 0
            $n = $n+1
        }
    }
    if($ede -eq "D"){
        #Match each character to associated encryption key
        foreach ($char in $paramCharVal) {
            foreach ($base in $encCharVal01){
                if($base -eq $char){
                    $encResult = $encResult+$baseCharVal[$i]  
                }
                $i = $i+1
            }
            $i = 0
            $n = $n+1
        }
    }

    return $encResult
}

# Split the line into an array
$cliVar = $a.Split(" ")

# Define encryption parameters 
$encCheckSum = $cliVar[0]
$encDecodeVal = $cliVar[1]
$encDE = $cliVar[2]

$encryptedResult = EncryptVal -ecs $encCheckSum -edv $encDecodeVal -ede $encDE
Write-Host $encryptedResult
