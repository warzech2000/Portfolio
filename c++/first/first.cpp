#include <iostream>

int main()
{
    // Początkowy dialog
    std::cout << std::endl;
    std::cout << "Oj byczku widze ze chcesz wykrasc moje kryptowaluty";
    std::cout << std::endl;
    std::cout << "Bedziesz musial przejsc przez siec moich zabezpieczen";
    std::cout << std::endl;

    //Declare 3 numbers
    const int CodeA = 4;
    const int CodeB = 6;
    const int CodeC = 8;

    const int CodeSum = CodeA + CodeB + CodeC;
    const int CodeProd = CodeA * CodeB * CodeC;

    //Print sum and mul to terminal
    std::cout << std::endl;
    std::cout << "-- Kod sklada sie z 3 cyfer odzielonych spacjami" <<std::endl;
    std::cout << "-- Suma tych cyfer wynosi: " << CodeSum << std::endl;
    std::cout << "-- Natomiast mnozac je przez siebie otrzymasz: " << CodeProd << std::endl;
    
    // Enter from terminal
    int GuessA, GuessB, GuessC;
    std::cin >> GuessA;
    std::cin >> GuessB;
    std::cin >> GuessC;

    // Guess Sum & Prod
    int GuessSum = GuessA + GuessB + GuessC;
    int GuessProd = GuessA * GuessB * GuessC;

    if (GuessSum==CodeSum && GuessProd==CodeProd)
    {   
        std::cout << "Przeszedles jeden poziom zabezpeczen." << std::endl;
        std::cout << "Przed toba jeszcze: " << std::endl;
    }
    else {
        std::cout << "Niestety nie udalo ci sie ;(";
    }

    return 0;
}