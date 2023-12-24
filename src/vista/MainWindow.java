/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package vista;


import java.io.IOException;
import java.io.InputStream;
import java.io.ObjectInputStream;
import java.io.Serializable;
import java.util.HashMap;
import javax.swing.DefaultListModel;
import modelo.Definition;
import modelo.Language;
import modelo.Reading;
import modelo.SentenceExample;
import modelo.Yojijukugo;

/**
 *
 * @author f_776
 */
public class MainWindow extends javax.swing.JFrame implements Serializable {

    private static HashMap<Integer, Yojijukugo> wordsHashMap;
    private static HashMap<Integer, Language> languageHashMap;
    private static HashMap<Integer, Definition[]> defHashMap;
    private static HashMap<Integer, Reading[]> readingHashMap;
    private static HashMap<Integer, SentenceExample[]> sentenceSampleHashMap;


    /**
     * Creates new form MainWindow
     */
    public MainWindow() {
       
        initComponents();
        //fetchDataFromDB();     
        loadAllObjects();
        //exportAllHashMaps();
        fillWordList();
        setLocationRelativeTo(null);
    }
    
//    private void exportAllHashMaps(){
//        exportObject(wordsHashMap, "src/main/resources/Objects/wordsHashSet");
//        exportObject(languageHashMap, "src/main/resources/Objects/languageHashSet");
//        exportObject(defHashMap, "src/main/resources/Objects/defHashSet");
//        exportObject(readingHashMap, "src/main/resources/Objects/readingHashMap");
//        exportObject(sentenceSampleHashMap, "src/main/resources/Objects/sentenceSampleHashMap");
//    }
//    
//    private void exportObject(Object o, String path) {
//
//        try (FileOutputStream fileOut = new FileOutputStream(path + ".ser"); ObjectOutputStream out = new ObjectOutputStream(fileOut)) {
//
//            out.writeObject(o);
//            System.out.println("Object " + path + " saved!");
//            fileOut.close();
//            out.close();
//
//        } catch (IOException i) {
//            System.out.println(i);
//        }
//    }

    
    @SuppressWarnings("unchecked")
    private <T> T loadObjectFromResource(String resourceName) {
        try (InputStream inputStream = MainWindow.class.getClassLoader().getResourceAsStream(resourceName)) {
            if (inputStream != null) {
                try (ObjectInputStream objectInputStream = new ObjectInputStream(inputStream)) {
                    //System.out.println(resourceName + " loaded");
                    // The cast is safe because we are reading an object of type T from the stream
                    return (T) objectInputStream.readObject();
                } catch (ClassNotFoundException e) {
                    // Handle the exception appropriately

                }
            } else {
                System.err.println("Resource not found: " + resourceName);
            }
        } catch (IOException e) {
            // Handle the exception appropriately

        }
        return null;
    }

    private void loadAllObjects() {
        wordsHashMap = loadObjectFromResource("Objects/wordsHashSet.ser");
        languageHashMap = loadObjectFromResource("Objects/languageHashSet.ser");
        defHashMap = loadObjectFromResource("Objects/defHashSet.ser");
        readingHashMap = loadObjectFromResource("Objects/readingHashMap.ser");
        sentenceSampleHashMap = loadObjectFromResource("Objects/sentenceSampleHashMap.ser");
    }

    private void fillWordList() {
        DefaultListModel<String> model = new DefaultListModel<>();

        for (Integer key : wordsHashMap.keySet()) {
            model.addElement(wordsHashMap.get(key).getWord());
        }

        lstWords.setModel(model);
    }

//    private void fetchDataFromDB() {
//        try (Connection connection = Conexion.getInstance().getConnection()) {
//            // Getting Data
//            MainWindow.wordsHashMap = ft.getYojijukugoMap(connection);
//            MainWindow.languageHashMap = ft.getLanguage(connection);
//            MainWindow.readingHashMap = ft.getReading(connection, wordsHashMap);
//            MainWindow.defHashMap = ft.getDefinition(connection, wordsHashMap, languageHashMap);
//            MainWindow.sentenceSampleHashMap = ft.getSentenceSamples(connection, wordsHashMap, languageHashMap);
//            
//        } catch (SQLException | URISyntaxException e) {
//            System.out.println(e);
//        } catch (Exception e) {
//            System.out.println(e);
//        }
//    }

    private Yojijukugo findWord(String word) {

        for (Integer key : wordsHashMap.keySet()) {
            if (wordsHashMap.get(key).getWord().equals(word)) {
                return wordsHashMap.get(key);
            }
        }
        return null;
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        pnlMain = new javax.swing.JPanel();
        jLabel1 = new javax.swing.JLabel();
        lblBackground = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        jSeparator1 = new javax.swing.JSeparator();
        jScrollPane1 = new javax.swing.JScrollPane();
        lstWords = new javax.swing.JList<>();
        jScrollPane2 = new javax.swing.JScrollPane();
        txtDef = new javax.swing.JTextArea();
        txtSearch = new javax.swing.JTextField();
        lblSearch = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Yojijukugo Dictionary");
        setResizable(false);

        pnlMain.setBackground(new java.awt.Color(255, 255, 255));
        pnlMain.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jLabel1.setIcon(new javax.swing.ImageIcon(getClass().getResource("/images/logo.jpeg")));
        pnlMain.add(jLabel1, new org.netbeans.lib.awtextra.AbsoluteConstraints(40, 30, 150, 150));

        lblBackground.setIcon(new javax.swing.ImageIcon(getClass().getResource("/images/background.jpeg")));
        pnlMain.add(lblBackground, new org.netbeans.lib.awtextra.AbsoluteConstraints(630, 0, -1, -1));

        jLabel2.setFont(new java.awt.Font("Yu Gothic UI", 0, 36)); // NOI18N
        jLabel2.setForeground(new java.awt.Color(0, 0, 255));
        jLabel2.setText("四字熟語 Dictionary");
        pnlMain.add(jLabel2, new org.netbeans.lib.awtextra.AbsoluteConstraints(240, 70, 320, 50));

        jSeparator1.setForeground(new java.awt.Color(204, 204, 204));
        pnlMain.add(jSeparator1, new org.netbeans.lib.awtextra.AbsoluteConstraints(210, 130, 370, -1));

        lstWords.setFont(new java.awt.Font("Yu Mincho", 0, 18)); // NOI18N
        lstWords.setSelectionMode(javax.swing.ListSelectionModel.SINGLE_SELECTION);
        lstWords.addListSelectionListener(new javax.swing.event.ListSelectionListener() {
            public void valueChanged(javax.swing.event.ListSelectionEvent evt) {
                lstWordsValueChanged(evt);
            }
        });
        jScrollPane1.setViewportView(lstWords);

        pnlMain.add(jScrollPane1, new org.netbeans.lib.awtextra.AbsoluteConstraints(40, 240, 150, 280));

        txtDef.setEditable(false);
        txtDef.setColumns(20);
        txtDef.setFont(new java.awt.Font("Yu Mincho", 0, 24)); // NOI18N
        txtDef.setLineWrap(true);
        txtDef.setRows(5);
        txtDef.setWrapStyleWord(true);
        jScrollPane2.setViewportView(txtDef);

        pnlMain.add(jScrollPane2, new org.netbeans.lib.awtextra.AbsoluteConstraints(220, 150, 360, 370));

        txtSearch.setFont(new java.awt.Font("Yu Mincho", 0, 18)); // NOI18N
        pnlMain.add(txtSearch, new org.netbeans.lib.awtextra.AbsoluteConstraints(40, 190, 110, 40));

        lblSearch.setIcon(new javax.swing.ImageIcon(getClass().getResource("/images/magglass.jpeg")));
        lblSearch.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                lblSearchMouseClicked(evt);
            }
        });
        pnlMain.add(lblSearch, new org.netbeans.lib.awtextra.AbsoluteConstraints(150, 190, 40, 40));

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(pnlMain, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(pnlMain, javax.swing.GroupLayout.DEFAULT_SIZE, 550, Short.MAX_VALUE)
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void lstWordsValueChanged(javax.swing.event.ListSelectionEvent evt) {//GEN-FIRST:event_lstWordsValueChanged

        String selectedValue = lstWords.getSelectedValue();

        if (selectedValue != null) {
            Yojijukugo y = findWord(selectedValue);

            // Readings
        StringBuilder readings = new StringBuilder();
        Reading[] readingList = readingHashMap.get(y.getId());
        if (readingList != null) {
            for (Reading r : readingList) {
                readings.append(r.getReading()).append("\n");
            }
        }

        // Definitions
        StringBuilder definitions = new StringBuilder();
        Definition[] definitionsList = defHashMap.get(y.getId());
        if (definitionsList != null) {
            int counter = 0;
            for (Definition d : definitionsList) {
                counter++;
                definitions.append(String.valueOf(counter)).append(". ").append(d.getDefinition()).append("\n");
            }
        }

        // Sentences
        StringBuilder sentences = new StringBuilder();
        SentenceExample[] sentencesList = sentenceSampleHashMap.get(y.getId());
        if (sentencesList != null) {
            sentences.append("Sample Sentences:").append("\n");
            int counter = 0;
            for (SentenceExample s : sentencesList) {
                
                if(s.getYojijukugo().getId() == 1){
                    counter++;
                    sentences.append(String.valueOf(counter)).append(". ");
                }
                sentences.append(s.getSentence()).append("\n");
            }
        }
            
            // Display the information
            txtDef.setText(y.getWord() + "\n" + readings.toString() + definitions.toString() + sentences.toString());
        }


    }//GEN-LAST:event_lstWordsValueChanged

    private void lblSearchMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_lblSearchMouseClicked
        // TODO add your handling code here:
        String text = txtSearch.getText();

        DefaultListModel<String> model = (DefaultListModel<String>) lstWords.getModel();

        for (int i = 0; i < model.size(); i++) {
            String value = model.getElementAt(i);
            if (value.contains(text)) {
                lstWords.setSelectedValue(value, true);
            }
        }

        //lstWords.setSelectedValue(text, true);
    }//GEN-LAST:event_lblSearchMouseClicked

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(MainWindow.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(MainWindow.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(MainWindow.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(MainWindow.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new MainWindow().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JScrollPane jScrollPane2;
    private javax.swing.JSeparator jSeparator1;
    private javax.swing.JLabel lblBackground;
    private javax.swing.JLabel lblSearch;
    private javax.swing.JList<String> lstWords;
    private javax.swing.JPanel pnlMain;
    private javax.swing.JTextArea txtDef;
    private javax.swing.JTextField txtSearch;
    // End of variables declaration//GEN-END:variables
}
