 Да, я могу предоставить пример программы для создания простого смарт-контракта на Ethereum. 

Вот пример контракта на Solidity, который позволяет депонировать Ether в контракт и затем выводить его обратно отправителю:

```solidity
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract SimpleStorage {

    mapping (address => uint) public balances;

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw() public {
        uint amount = balances[msg.sender];
        balances[msg.sender] = 0;
        (bool sent, ) = msg.sender.call{value: amount}("");
        require(sent, "Failed to send Ether");
    }
}
```

Этот контракт хранит балансы отправителей в mapping, позволяет пользователям депонировать Ether с помощью функции `deposit`, и затем выводить с помощью `withdraw`. 

Чтобы развернуть этот контракт, можно использовать какой-нибудь Ethereum клиент как MetaMask, и вызвать соответствующие функции для взаимодействия с контрактом.

Надеюсь, этот пример даст представление о том, как можно создавать и использовать смарт-контракты на Solidity. Если нужны какие-то пояснения или есть дополнительные вопросы - пожалуйста, дайте мне знать!
