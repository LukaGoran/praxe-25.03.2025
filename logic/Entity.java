package org.example.logic;

import javax.swing.*;
import java.awt.*;

public class Entity {
    public Coordinates coord;
    public Image image;

    public Entity(int x, int y, String url) {
        this.coord = new Coordinates(x,y);
        ImageIcon ii = new ImageIcon(getClass().getResource("/" + url));
        image = ii.getImage();
    }

    public Rectangle getEntityRectangle(){
        return new Rectangle(coord.x, coord.y, image.getWidth(null), image.getHeight(null));
    }

    public void move(int steps, Direction direction){
        switch (direction){
            case UP -> {
                coord.y -= steps;
            }
            case DOWN -> {
                coord.y += steps;
            }
            case LEFT -> {
                coord.x -= steps;
            }
            case RIGHT -> {
                coord.x += steps;
            }
        }
    }

}


