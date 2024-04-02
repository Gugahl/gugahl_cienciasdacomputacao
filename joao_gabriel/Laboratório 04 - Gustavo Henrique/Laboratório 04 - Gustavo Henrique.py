{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMp9MnNxNYzSxhYyFAAcjvP"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dEqoCERaUECV",
        "outputId": "7449e1eb-d619-4fef-a573-b8103f685d64"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número inteiro: 2\n",
            "O número 2 é PAR.\n"
          ]
        }
      ],
      "source": [
        "\"\"\"\n",
        "  Laboratório 04\n",
        "   Exercício 01\n",
        "\"\"\"\n",
        "\n",
        "numero = int(input(\"Digite um número inteiro: \"))\n",
        "print(f'O número {numero} é ', end='')\n",
        "if numero % 2 == 0:\n",
        "  print(\"PAR.\")\n",
        "else:\n",
        "  print(\"ÍMPAR.\")\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\"\"\"\n",
        "  Laboratório 04\n",
        "   Exercício 02\n",
        "\"\"\"\n",
        "\n",
        "salario = float(input(\"Qual é o valor do seu salário? R$\"))\n",
        "print(\"Seu novo salário é de R$\", end='')\n",
        "if salario < 2000:\n",
        "  novo_salario = (salario * 1.1) + 200\n",
        "  print(f\"{novo_salario:.2f}\")\n",
        "elif salario < 5000:\n",
        "  novo_salario = (salario * 1.08) + 150\n",
        "  print(f\"{novo_salario:.2f}\")\n",
        "else:\n",
        "  novo_salario = salario * 1.05\n",
        "  print(f\"{novo_salario:.2f}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Gxc7kvf-Vuei",
        "outputId": "7b3bb30c-0393-41aa-927b-400b28a3ebd7"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Qual é o valor do seu salário? R$2000\n",
            "Seu novo salário é R$2310.00\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\"\"\"\n",
        "  Laboratório 04\n",
        "   Exercício 03\n",
        "\"\"\"\n",
        "\n",
        "idade = float(input(f\"Quantos anos, humanos, de vida seu cachorro tem? \"))\n",
        "print(f\"Seu cachorro tem \", end='')\n",
        "if idade < 3:\n",
        "  anos_dog = 10.5 * idade\n",
        "  print(f'{anos_dog} anos.')\n",
        "else:\n",
        "  anos_dog = (10.5 * 2) + ((idade - 2) * 4)\n",
        "  print(f'{anos_dog} anos.')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "E9Sbe25KX2ix",
        "outputId": "87b15745-73fd-47c1-f2cc-3281c7a4f2e2"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Quantos anos, humanos, de vida seu cachorro tem? 4\n",
            "Seu cachorro tem 29.0 anos.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\"\"\"\n",
        "  Laboratório 04\n",
        "   Exercício 04\n",
        "\"\"\"\n",
        "\n",
        "numero1 = int(input(\"Digite um número inteiro: \"))\n",
        "numero2 = int(input(\"Digite um número inteiro: \"))\n",
        "numero3 = int(input(\"Digite um número inteiro: \"))\n",
        "numero4 = int(input(\"Digite um número inteiro: \"))\n",
        "soma = numero3 + numero4\n",
        "multiplicação = numero3 * numero4\n",
        "print(f\"A soma de {numero3} e {numero4}, que resulta em {soma}\", end='')\n",
        "print(f\" está dentro da faixa.\" if numero1 < soma < numero2 else f' não está dentro da faixa.')\n",
        "print(f\"A multiplicação de {numero3} * {numero4}, que resulta em {multiplicação}\", end='')\n",
        "print(f\" está dentro da faixa.\" if numero1 < multiplicação < numero2 else f' não está dentro da faixa.')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0QjXgaWgZ1AS",
        "outputId": "0f1a5e96-bc4c-4f11-fc6b-36554496ea5c"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número inteiro: 1\n",
            "Digite um número inteiro: 23\n",
            "Digite um número inteiro: 24\n",
            "Digite um número inteiro: 25\n",
            "A soma de 24 e 25, que resulta em 49 não está dentro da faixa.\n",
            "A multiplicação de 24 * 25, que resulta em 600 não está dentro da faixa.\n"
          ]
        }
      ]
    }
  ]
}
