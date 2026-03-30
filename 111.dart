void main(){
  int num1 = 10;
  double num2 = 3.141592;

  String str1 = num1.toString();
  String str2 = num1.toStringAsFixed(2);
  print('num1 to str is $str1');
  print('num2 to str is $str2');

  num1 = int.parse('-12');
  num2 = double.parse('123.4567');
  print(num1);
  print(num2);
  print('${num.parse('-34.56')}');

  String? firstname;
  String sirname;
  print('Value:$firstname');

}
