class Solution {
    public boolean isAnagram(String s, String t) {
     int f=0;
     int a=0;
     int b=0;
    for (char c='a';c<='z';c++)
    {
        if(s.length()==t.length())
        {
            for (int i=0;i<s.length();i++)
            {
                if (s.charAt(i)==c)
                a++;
                if (t.charAt(i)==c)
                b++;
            }
            if(a!=b)
            return false;
        }
        else
        return false;
    }
    return true;
    }
}
