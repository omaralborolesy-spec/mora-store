import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(page_title="MORA STORE", page_icon="🛍️", layout="centered")

# --- إدارة حالة الجلسة ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# --- تصميم الألوان والأشكال (CSS) ---
st.markdown("""
    <style>
        .stApp {
            background-color: #f4f7f6;
        }
        h1, h2, h3 {
            color: #2c3e50;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
        }
        div.stButton > button {
            background-color: #3498db;
            color: white;
            border-radius: 20px;
            border: none;
            padding: 10px 24px;
            font-size: 16px;
            font-weight: bold;
            transition: all 0.3s ease;
            width: 100%;
        }
        div.stButton > button:hover {
            background-color: #2980b9;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        div.stTextInput > div > div > input {
            border-radius: 10px;
            border: 1px solid #bdc3c7;
        }
    </style>
""", unsafe_allow_html=True)

# --- صفحة تسجيل الدخول ---
def show_login_page():
    st.markdown("<h1>🛍️ MORA STORE</h1>", unsafe_allow_html=True)
    st.markdown("<h3>مرحباً بك، يرجى تسجيل الدخول للبدء</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.write("---")
        username = st.text_input("اسم المستخدم", placeholder="ادخل اسمك هنا...")
        password = st.text_input("كلمة المرور", type="password", placeholder="••••••••")
        
        login_button = st.button("تسجيل الدخول")
        
        if login_button:
            if username.lower() == "omar" and password == "12345":
                st.session_state['logged_in'] = True
                st.success("تم تسجيل الدخول بنجاح! جاري تحويلك...")
                st.rerun()
            elif username == "" or password == "":
                 st.warning("الرجاء إدخال اسم المستخدم وكلمة المرور.")
            else:
                st.error("عفواً، اسم المستخدم أو كلمة المرور غير صحيحة.")

# --- صفحة المنتجات ---
def show_products_page():
    st.markdown("<h1>👕 MORA CLOTHING COLLECTION 👖</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #7f8c8d;'>أحدث تصميمات MORA الفخمة</p>", unsafe_allow_html=True)
    st.write("---")
    
    # روابط الصور الجاهزة المباشرة
    hoodie_img = "https://i.ibb.co/60HsnQv/mora-hoodie.png"
    pants_img = "https://i.ibb.co/Xz9tHnF/mora-pants.png"
    suit_img = "https://i.ibb.co/mHn2Xz1/mora-suit.png"

    # قسم الهودي والشروال
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("هودي MORA الأسود")
        st.image("tshirt.jpg", use_column_width=True) # لو الصورة محلياً
        st.markdown("**السعر:** 450 جنيه")
        st.write("خامة قطنية ثقيلة وممتازة بتطريز عالي الجودة.")
        st.button("إضافة للعربة", key="tshirt_btn")

    with col2:
        st.subheader("شروال MORA الرياضي")
        st.image("pants.jpg", use_column_width=True) # لو الصورة محلياً
        st.markdown("**السعر:** 350 جنيه")
        st.write("شروال بتصميم مريح جداً وعصري.")
        st.button("إضافة للعربة", key="pants_btn")

    st.write("---")
    
    # قسم الطقم الكامل
    st.subheader("🔥 الطقم الكامل (تيشرت + شروال)")
    col_c1, col_c2, col_c3 = st.columns([1,2,1])
    with col_c2:
        st.image("full_suit.jpg", use_column_width=True) # لو الصورة محلياً
        st.markdown("**السعر:** 750 جنيه (وفر أكثر)")
        st.write("احصل على الطقم الكامل المتكامل بتصميم موحد.")
        st.button("إضافة الطقم للعربة", key="suit_btn")

    # زر تسجيل الخروج
    st.write("---")
    col_out1, col_out2, col_out3 = st.columns([1,1,1])
    with col_out2:
        if st.button("تسجيل الخروج"):
            st.session_state['logged_in'] = False
            st.rerun()

# --- التوجيه التلقائي ---
if st.session_state['logged_in']:
    show_products_page()
else:
    show_login_page()