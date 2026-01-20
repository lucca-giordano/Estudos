package POO;

public class Player {

    private int life = 100;

    public void atackEnemy(Enemy enemy){
        enemy.life--;
    }

}
