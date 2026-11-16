Сегодня тестировал импорт PyTorch.

1. Проверяем PyTorch
python -c "import torch; print(torch.__version__)"  >>> result 2.x.x
2. Проверяем, что PyTorch действительно работает
python -c "import torch; x = torch.tensor([1, 2, 3]); print(x); print(x * 2)" >>> result
tensor([1, 2, 3])
tensor([2, 4, 6])
3. Проверяем доступность GPU
python -c "import torch; print(torch.cuda.is_available())" >>> result False

вывод:
создал тензор — структуру данных, с которой работает PyTorch.
PyTorch выполнил операцию сразу над всеми элементами
Пока достаточно запомнить, что тензоры — один из фундаментальных инструментов Deep Learning.

-------------------------------------------------------------------------------
