import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ScriptRunner {
    private JFrame frame;
    private JPanel mainPanel;
    private JButton menuButton;
    private JPanel menuContainer;
    private boolean menuExpanded = false;
    private List<ScriptInfo> scripts = new ArrayList<>();
    private List<JButton> scriptButtons = new ArrayList<>();
    private int expandedHeight;
    private final int BUTTON_SIZE = 35;
    private final int ANIMATION_DURATION = 300;

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            try {
                new ScriptRunner().createAndShowGUI();
            } catch (Exception e) {
                e.printStackTrace();
            }
        });
    }

    private void createAndShowGUI() {
        // Create main frame
        frame = new JFrame();
        frame.setUndecorated(true);
        frame.setAlwaysOnTop(true);
        frame.setBackground(new Color(0, 0, 0, 0));

        // Main panel
        mainPanel = new JPanel();
        mainPanel.setLayout(new BoxLayout(mainPanel, BoxLayout.Y_AXIS));
        mainPanel.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));
        mainPanel.setOpaque(false);

        // Menu button
        menuButton = createIconButton("images/menu.png", "Menu");
        menuButton.addActionListener(e -> toggleMenu());
        mainPanel.add(Box.createVerticalGlue());
        mainPanel.add(menuButton);
        mainPanel.add(Box.createVerticalGlue());
        menuButton.setAlignmentX(Component.CENTER_ALIGNMENT);

        // Menu container
        menuContainer = new JPanel();
        menuContainer.setLayout(new BoxLayout(menuContainer, BoxLayout.Y_AXIS));
        menuContainer.setMaximumSize(new Dimension(BUTTON_SIZE + 10, 0));
        menuContainer.setOpaque(false);
        menuContainer.setBorder(BorderFactory.createEmptyBorder(0, 0, 0, 0));
        mainPanel.add(menuContainer);

        // Load scripts
        loadScriptsFromFile("scripts.txt");

        // Create script buttons
        for (ScriptInfo script : scripts) {
            JButton btn = createIconButton(script.path, script.name);
            btn.addActionListener(e -> runScript(script.name));
            btn.setAlignmentX(Component.CENTER_ALIGNMENT);
            menuContainer.add(btn);
            menuContainer.add(Box.createVerticalStrut(10));
            scriptButtons.add(btn);
        }

        // Close button
        JButton closeBtn = createIconButton("images/close.png", "Close");
        closeBtn.addActionListener(e -> System.exit(0));
        closeBtn.setAlignmentX(Component.CENTER_ALIGNMENT);
        menuContainer.add(closeBtn);
        scriptButtons.add(closeBtn);

        // Calculate expanded height
        int spacing = 10;
        int numButtons = scriptButtons.size();
        expandedHeight = (BUTTON_SIZE * numButtons) + (spacing * (numButtons - 1));

        // Set up frame
        frame.add(mainPanel);
        frame.setSize(60, 400);
        positionWindow();
        frame.setVisible(true);

        // Make window draggable
        MouseAdapter ma = new MouseAdapter() {
            private Point initialClick;

            @Override
            public void mousePressed(MouseEvent e) {
                initialClick = e.getPoint();
            }

            @Override
            public void mouseDragged(MouseEvent e) {
                int thisX = frame.getLocation().x;
                int thisY = frame.getLocation().y;

                int xMoved = e.getX() - initialClick.x;
                int yMoved = e.getY() - initialClick.y;

                frame.setLocation(thisX + xMoved, thisY + yMoved);
            }
        };

        mainPanel.addMouseListener(ma);
        mainPanel.addMouseMotionListener(ma);
    }

    private JButton createIconButton(String iconPath, String tooltip) {
        JButton btn = new JButton();
        btn.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));
        btn.setToolTipText(tooltip);
        
        try {
            ImageIcon icon = new ImageIcon(iconPath);
            Image scaled = icon.getImage().getScaledInstance(BUTTON_SIZE, BUTTON_SIZE, Image.SCALE_SMOOTH);
            btn.setIcon(new ImageIcon(scaled));
        } catch (Exception e) {
            System.err.println("Error loading icon: " + iconPath);
        }
        
        btn.setPreferredSize(new Dimension(BUTTON_SIZE + 4, BUTTON_SIZE + 4));
        btn.setMaximumSize(new Dimension(BUTTON_SIZE + 4, BUTTON_SIZE + 4));
        btn.setBorderPainted(false);
        btn.setContentAreaFilled(false);
        btn.setFocusPainted(false);
        btn.setOpaque(false);
        
        // Hover effects
        btn.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseEntered(MouseEvent e) {
                btn.setOpaque(true);
                btn.setBackground(Color.BLUE);
            }

            @Override
            public void mouseExited(MouseEvent e) {
                btn.setOpaque(false);
                btn.setBackground(null);
            }

            @Override
            public void mousePressed(MouseEvent e) {
                btn.setOpaque(true);
                btn.setBackground(Color.GREEN);
            }

            @Override
            public void mouseReleased(MouseEvent e) {
                btn.setOpaque(true);
                btn.setBackground(Color.BLUE);
            }
        });
        
        return btn;
    }

    private void loadScriptsFromFile(String filepath) {
        try (BufferedReader br = new BufferedReader(new FileReader(filepath))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.split(",");
                if (parts.length >= 2) {
                    scripts.add(new ScriptInfo(parts[0].trim(), parts[1].trim()));
                }
            }
        } catch (IOException e) {
            System.err.println("Warning: " + filepath + " not found. No scripts loaded.");
        }
    }

    private void runScript(String scriptName) {
        try {
            ProcessBuilder pb = new ProcessBuilder("python", scriptName + ".py");
            pb.start();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void toggleMenu() {
        if (menuExpanded) {
            collapseMenu();
        } else {
            expandMenu();
        }
        menuExpanded = !menuExpanded;
    }

    private void expandMenu() {
        menuContainer.setMaximumSize(new Dimension(BUTTON_SIZE + 10, expandedHeight));
        frame.pack();
    }

    private void collapseMenu() {
        menuContainer.setMaximumSize(new Dimension(BUTTON_SIZE + 10, 0));
        frame.pack();
    }

    private void positionWindow() {
        GraphicsEnvironment ge = GraphicsEnvironment.getLocalGraphicsEnvironment();
        GraphicsDevice defaultScreen = ge.getDefaultScreenDevice();
        Rectangle rect = defaultScreen.getDefaultConfiguration().getBounds();
        frame.setLocation(rect.width - frame.getWidth(), (rect.height - frame.getHeight()) / 2);
    }

    private static class ScriptInfo {
        String name;
        String path;

        ScriptInfo(String name, String path) {
            this.name = name;
            this.path = path;
        }
    }
}