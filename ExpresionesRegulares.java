import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.net.URL;

public class newJavaFile extends JFrame {

    private JTextField campo1, campo2, campo3, campo4;
    private JLabel mensajeCampo1, mensajeCampo2, mensajeCampo3, mensajeCampo4;

    public newJavaFile() {
        initComponents();
    }

    private void initComponents() {
        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Formulario Java");

        JPanel panel = new JPanel(new GridLayout(4, 3));

        campo1 = new JTextField();
        campo2 = new JTextField();
        campo3 = new JTextField();
        campo4 = new JTextField();
        mensajeCampo1 = new JLabel();
        mensajeCampo2 = new JLabel();
        mensajeCampo3 = new JLabel();
        mensajeCampo4 = new JLabel();

        JButton boton1 = new JButton("Validar IP");
        JButton boton2 = new JButton("Validar MAC");
        JButton boton3 = new JButton("Validar RFC");
        JButton boton4 = new JButton("Validar URL");

        // Agregar ActionListener al botón 1 para validar la IP
        boton1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String ip = campo1.getText();
                if (validarIP(ip)) {
                    mensajeCampo1.setText("Es una dirección IP válida");
                } else {
                    mensajeCampo1.setText("No es una dirección IP válida");
                }
            }
        });

        // Agregar ActionListener al botón 2 para validar la MAC
        boton2.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String mac = campo2.getText();
                if (validarMAC(mac)) {
                    mensajeCampo2.setText("Es una dirección MAC válida");
                } else {
                    mensajeCampo2.setText("No es una dirección MAC válida");
                }
            }
        });

        // Agregar ActionListener al botón 3 para validar el RFC
        boton3.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String rfc = campo3.getText();
                if (validarRFC(rfc)) {
                    mensajeCampo3.setText("Es un RFC válido");
                } else {
                    mensajeCampo3.setText("No es un RFC válido");
                }
            }
        });

        // Agregar ActionListener al botón 4 para validar la URL
        boton4.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String url = campo4.getText();
                if (validarURL(url)) {
                    mensajeCampo4.setText("Es una URL válida");
                } else {
                    mensajeCampo4.setText("No es una URL válida");
                }
            }
        });

        panel.add(new JLabel("Campo 1 (IP):"));
        panel.add(campo1);
        panel.add(boton1);
        panel.add(mensajeCampo1);

        panel.add(new JLabel("Campo 2 (MAC):"));
        panel.add(campo2);
        panel.add(boton2);
        panel.add(mensajeCampo2);

        panel.add(new JLabel("Campo 3 (RFC):"));
        panel.add(campo3);
        panel.add(boton3);
        panel.add(mensajeCampo3);

        panel.add(new JLabel("Campo 4 (URL):"));
        panel.add(campo4);
        panel.add(boton4);
        panel.add(mensajeCampo4);

        getContentPane().add(panel);
        pack();
    }

    private boolean validarIP(String ip) {
        // Patrón de validación para una dirección IP
        String ipPattern = "^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$";
        Pattern pattern = Pattern.compile(ipPattern);
        Matcher matcher = pattern.matcher(ip);
        return matcher.matches();
    }

    private boolean validarMAC(String mac) {
        // Patrón de validación para una dirección MAC
        String macPattern = "^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$";
        Pattern pattern = Pattern.compile(macPattern);
        Matcher matcher = pattern.matcher(mac);
        return matcher.matches();
    }

    private boolean validarRFC(String rfc) {
        // Patrón de validación para un RFC en México (simplificado)
        String rfcPattern = "^[A-Z]{4}[0-9]{6}[A-Z0-9]{3}$";
        Pattern pattern = Pattern.compile(rfcPattern);
        Matcher matcher = pattern.matcher(rfc);
        return matcher.matches();
    }

    private boolean validarURL(String url) {
        try {
            new URL(url);
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    public static void main(String args[]) {
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new newJavaFile().setVisible(true);
            }
        });
    }
}
