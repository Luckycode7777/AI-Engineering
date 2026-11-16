1. Сегодня тестировал импорт PyTorch.
Проверяем PyTorch
python -c "import torch; print(torch.__version__)"  >>> result 2.x.x
Проверяем, что PyTorch действительно работает
python -c "import torch; x = torch.tensor([1, 2, 3]); print(x); print(x * 2)" >>> result
tensor([1, 2, 3])
tensor([2, 4, 6])
Проверяем доступность GPU
python -c "import torch; print(torch.cuda.is_available())" >>> result False


создал тензор — структуру данных, с которой работает PyTorch.
PyTorch выполнил операцию сразу над всеми элементами
Пока достаточно запомнить, что тензоры — один из фундаментальных инструментов Deep Learning.

-------------------------------------------------------------------------------
