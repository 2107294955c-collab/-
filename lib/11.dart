// void main(){
//    String firstname = 'gildong';
//    String sirname = 'Hong';
//    String fullname = '$sirname $firstname';
//    print('Name is $fullname');
// }
void main() {
  int num1 = 10;
  double pi = 3.14;
  double num3 = num1 * pi;
  num num4 = num1 * pi;

  print(num3);
  print(num4);

  String firstname = 'nak';
  String sirname = 'Heo';
  String fullname;
  fullname = '$sirname $firstname';
  print('Hello, $firstname');
  print('$fullname :${fullname.length}');

  bool aa = false;
  bool bb = (num1>0);
  bool chk  = aa & bb;
  print('check result is $chk');
}