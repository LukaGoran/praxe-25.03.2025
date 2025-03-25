package org.example;

import org.example.logic.Enemy;

import javax.swing.*;
import java.awt.*;
import java.awt.image.ImageObserver;

public class GameGraphics extends JFrame {
    GameLogic logic;
    Draw draw;

    public GameGraphics(GameLogic logic) throws HeadlessException {
        this.logic = logic;

        draw = new Draw();
        add(draw);

        setExtendedState(MAXIMIZED_BOTH);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        // musí být dole v konstruktoru
        setVisible(true);

    }

    public void render(GameLogic logic) {
        this.logic = logic;
        // volá metodu paintComponent v Draw
        repaint();
    }


    private class Draw extends JPanel {
        @Override
        protected void paintComponent(Graphics g) {
            g.drawImage(logic.background.image, logic.background.coord.x, logic.background.coord.y, null);
            g.drawImage(logic.ball.image, logic.ball.coord.x, logic.ball.coord.y, null);

            for (Enemy enemy: logic.enemies){
                g.drawImage(enemy.image, enemy.coord.x, enemy.coord.y, null);
            }
        }
    }
}


