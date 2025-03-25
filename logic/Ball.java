package org.example.logic;

import java.awt.*;
import java.util.ArrayList;

public class Ball extends Entity {
    public Ball(int x, int y, String url) {
        super(x, y, url);
    }
    public ArrayList<Coordinates> getAllCoordinates() {
        ArrayList<Coordinates> ballCoords = new ArrayList<>();
        for (int i = coord.x; i < coord.x + image.getWidth(null); i++) {
            for (int j = coord.y; j < coord.y + image.getHeight(null); j++) {
                ballCoords.add(new Coordinates(i, j));
            }
        }
        return ballCoords;

}
    }