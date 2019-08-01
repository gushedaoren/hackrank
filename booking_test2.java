import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;

import javax.xml.parsers.ParserConfigurationException;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.LinkedList;

class Seeker {

    public static View findViewById(ViewGroup root, int id) {

        
        // implement this method only
        for(int i=0;i<root.getChildCount();i++){
            View child=root.getChildAt(i);
           

            if(child.getId()==id){
                return child;
            }
            if(child.getName().equals("ViewGroup")){
               ViewGroup vg=child;
               for(int j=0;j<vg.getChildCount();j++){
                   View child2=vg.getChildAt(j);
                   if(child2.getId()==2){
                       return child2;
                   }
               }
            }
          
            
        }
        
        return "";
    }
}
// don’t edit code below this line

// this code is not editable
//                                               ∆
//                                               |
//                                               |
// please focus on implementing the method above |

class View {
    private ViewGroup parent;
    private String name;
    private int id;

    View(ViewGroup parent) {
        this.parent = parent;
    }

    public int getId() {
        return id;
    }

    public ViewGroup getParent() {
        return parent;
    }

    void setId(int id) {
        this.id = id;
    }

    void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}

class ViewGroup extends View {
    private ArrayList<View> children = new ArrayList<>();

    ViewGroup(ViewGroup parent) {
        super(parent);
    }

    void addChild(View child) {
        children.add(child);
    }

    public int getChildCount() {
        return children.size();
    }
    public View getChildAt(int index) {
        return children.get(index);
    }
}

public class Main {
    public static void main(String[] args) throws ParserConfigurationException, SAXException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        int id = Integer.parseInt(line);
        StringBuilder builder = new StringBuilder();

        while ((line = br.readLine()) != null) {
            builder.append(line);
            builder.append(' ');
        }
        View root = Parser.parse(builder.toString());
        View found = Seeker.findViewById((ViewGroup)root, id);
        if (found != null) {
            System.out.println(found.getName());
        } else {
            System.out.println(found);
        }
    }
}

class Parser {
    static View parse(String input) throws IOException, SAXException, ParserConfigurationException {
        SAXParserFactory factory = SAXParserFactory.newInstance();
        SAXParser saxParser = factory.newSAXParser();
        SaxHandler saxHandler = new SaxHandler();
        InputStream is = new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8));
        saxParser.parse(is, saxHandler);

        return saxHandler.getLast();
    }
}

class SaxHandler extends DefaultHandler {

    private View current;
    private View last;

    private boolean bName;
    private boolean bId;

    @Override
    public void startElement(String uri, String localName, String qName, Attributes attributes) throws SAXException {
        if (qName.equals("ViewGroup")) {
            ViewGroup parent = (ViewGroup)current;
            ViewGroup newParent = new ViewGroup(parent);
            if (parent != null) {
                parent.addChild(newParent);
            }
            current = newParent;
        } else if (qName.equals("View")) {
            ViewGroup parent = (ViewGroup)current;
            View newView = new View(parent);
            parent.addChild(newView);
            current = newView;
        } else if (qName.equals("name")) {
            bName = true;
        } else if (qName.equals("id")) {
            bId = true;
        }
    }

    @Override
    public void endElement(String uri, String localName, String qName) throws SAXException {
        if (qName.equals("ViewGroup") ||
                qName.equals("View") ) {
            if (current != null) {
                last = current;
                current = current.getParent();
            }
        }
    }

    @Override
    public void characters(char[] ch, int start, int length) throws SAXException {
        if (bName) {
            current.setName(new String(ch, start, length));
            bName = false;
        } else if (bId) {
            String idString = new String(ch, start, length);
            int id = Integer.parseInt(idString);
            current.setId(id);
            bId = false;
        }
    }

    public View getLast() {
        return last;
    }
}