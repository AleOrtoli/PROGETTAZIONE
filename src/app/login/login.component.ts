import { RouterModule } from '@angular/router';
import { Component } from '@angular/core';
import {NgForm} from '@angular/forms';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; 
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [RouterModule, CommonModule, FormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  loginError: string = '';
  loginSuccess: string = '';
  private apiUrl = 'http://localhost:5000/login'; 
  
  constructor(private http: HttpClient) { }

  onLogin(loginForm: NgForm): void {
    if (loginForm.valid) {
      this.http.post<any>(this.apiUrl, loginForm.value ).subscribe(
        response => {
          console.log('success:', response);
          this.loginSuccess = 'Benvenuto.';
        },
        
        error => {
          console.error('Error during login:', error);
          // Verifica se l'errore contiene un messaggio specifico dal backend
          if (error.error && error.error.error) {
            this.loginError = error.error.error;
          } else {
            this.loginError = 'Credenziali di accesso errate. Riprova.';
          }
        }
      );
    } else {
      console.log('Form is invalid');
    }
  }
}
