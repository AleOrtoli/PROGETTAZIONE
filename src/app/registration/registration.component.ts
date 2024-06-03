import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import {NgForm} from '@angular/forms';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; 
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-registration',
  standalone: true,
  imports: [RouterModule, CommonModule, FormsModule
  ],
  templateUrl: './registration.component.html',
  styleUrl: './registration.component.css',
  
}) 
export class RegistrationComponent {
  private apiUrl = 'http://localhost:5001/registration';

  constructor(private http: HttpClient) {}

  onRegister(registerForm: NgForm) {
    if (registerForm.valid) {
      this.http.post<any>(this.apiUrl, registerForm.value).subscribe(
        response => {
          console.log('User registered successfully:', response);
          // Qui puoi aggiungere la logica per gestire una registrazione avvenuta con successo
        },
        error => {
          console.error('Error during registration:', error);
          // Qui puoi aggiungere la logica per gestire errori durante la registrazione
        }
      );
    } else {
      console.log('Form is invalid');
    }
  }
}
